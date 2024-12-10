package lab7


import org.apache.pekko.actor._
import scala.concurrent.duration._
import org.apache.pekko.actor.CoordinatedShutdown
import org.apache.pekko.actor.CoordinatedShutdown.UnknownReason
import org.apache.pekko.util.Timeout
import scala.concurrent.ExecutionContext.Implicits.global



/*
    Używając aktorów zaimplementuj "rozproszony licznik słów". Powinien on składać się z aktora głównego, typu:
        class Nadzorca extends Actor { ... }
    oraz dynamicznie określanej (w momencie inicjowania działania nadzorcy) liczby aktorów "roboczych", typu:
        class Pracownik extends Actor { ... }
    Po uruchomieniu, Nadzorca powinien być w stanie przyjąć jedynie komunikat inicjalizacyjny postaci
        case class Init(liczbaPracownikow: Int)
    w którego efekcie powinien utworzyć zadaną liczbę aktorów typu Pracownik i przejść do stanu, 
    w którym jest w stanie przyjmować "zlecenia" nadsyłane za pomocą komunikatów
        case class Zlecenie(tekst: List[String])
    Po otrzymaniu komunikatu Zlecenie nadzorca powinien zmienić swój stan oraz przekazywać poszczególne napisy z listy tekst do "obróbki" pracownikom. 
    Służyć do tego powinny komunikaty
        case class Wykonaj( /* argumenty */ )
    Pracownicy zwracają informację do nadzorcy odnośnie liczby znalezionych różnych słów w wersie (np. "Ulica" i "ulica" to identyczne słowa).
        case class Wynik( /* argumenty */ )
    Nadzorca sumuje/agreguje napływające wyniki oraz wysyła kolejny napis (jeżeli jeszcze jakiś istnieje) z listy tekst, 
    pracownikowi od którego otrzymał wynik. Po otrzymaniu wszystkich odpowiedzi od pracowników i wyliczeniu wszystkich słów z listy, 
    nadzorca wypisuje na konsoli wynik i wraca do stanu oczekiwania na kolejne zlecenie.
*/

class Boss extends Actor {
  def receive: Receive = {
    case msg => println(s"Odebrałem wiadomość: $msg")
  }
}

case class Init(liczbaPracownikow: Int)
case class Zlecenie(tekst: List[String])
case class Wykonaj(tekst: String)
case class Wynik(slow: Set[String])

class Nadzorca extends Actor {
  var pracownicy: List[ActorRef] = List()
  var oczekujaceZlecenia: List[String] = List()
  var wyniki: Set[String] = Set()
  var liczbaPracownikow: Int = 0

  def receive: Receive = {
    case Init(liczbaPracownikow) =>
      this.liczbaPracownikow = liczbaPracownikow
      pracownicy = (1 to liczbaPracownikow).map { i =>
        context.actorOf(Props(new Pracownik()), s"pracownik$i")
      }.toList
      context.become(przyjmowanieZlecen)
    
    case _ => println("Nieznany komunikat")
  }

  def przyjmowanieZlecen: Receive = {
    case Zlecenie(tekst) =>
      oczekujaceZlecenia = tekst
      wyniki = Set()
      pracownicy.zip(tekst).foreach { case (pracownik, linia) =>
        pracownik ! Wykonaj(linia)
      }
    
    case Wynik(slow) =>
      wyniki = wyniki ++ slow
      if (wyniki.size == oczekujaceZlecenia.size) {
        val sumaSlow = wyniki.size
        println(s"Liczba unikalnych słów: $sumaSlow")
        context.become(przyjmowanieZlecen)
      }
  }
}

class Pracownik extends Actor {
  def receive: Receive = {
    case Wykonaj(tekst) =>
      val slowa = tekst.split("\\s+").map(_.toLowerCase).toSet
      sender() ! Wynik(slowa)
  }
}


object ex2 extends App {
    def dane(): List[String] = scala.io.Source.fromResource("ogniem_i_mieczem.txt").getLines.toList
  
    val system = ActorSystem("WordCounterSystem")
    val nadzorca = system.actorOf(Props(new Nadzorca()), "nadzorca")

    nadzorca ! Init(3)
    nadzorca ! Zlecenie(List("To jest test", "To jest kolejny test", "Jeszcze jeden test"))

    system.scheduler.scheduleOnce(5.seconds) {
        system.terminate()
    }
}