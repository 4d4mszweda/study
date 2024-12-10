package lab7


/*
    Zdefiniuj klasę
        class Player extends Actor { ... }
    tak, aby po utworzeniu:
        dwóch aktorów typu Player mogli oni grać w "ping-ponga" (w nieskończoność wysyłali do siebie komunikat).
        trzech aktorów typu Player mogli oni grać w "ping-ponga" w trójkącie.
        listy, zawierającą dowolną liczbę aktorów typu Player, mogli oni grać w "ping-ponga" po okręgu. 
*/


import org.apache.pekko.actor._
import scala.concurrent.duration._
import org.apache.pekko.actor.CoordinatedShutdown
import org.apache.pekko.actor.CoordinatedShutdown.UnknownReason
import org.apache.pekko.util.Timeout
import scala.concurrent.ExecutionContext.Implicits.global


class Player(var nextPlayer: ActorRef) extends Actor {
    def receive: Receive = {
        case Player.SetNextPlayer(player) =>
            nextPlayer = player
        case "ping" =>
            println(s"${self.path.name} received ping")
            nextPlayer ! "pong"
        case "pong" =>
            println(s"${self.path.name} received pong")
            nextPlayer ! "ping"
    }
}

object Player {
    case class SetNextPlayer(player: ActorRef)
}


object ex1 extends App {
    val system = ActorSystem("PingPongSystem")

    val player1 = system.actorOf(Props(new Player(null)), "player1")
    val player2 = system.actorOf(Props(new Player(player1)), "player2")
    player1 ! Player.SetNextPlayer(player2)

    player1 ! "ping"

    system.scheduler.scheduleOnce(2.seconds) {
        player1 ! PoisonPill
        player2 ! PoisonPill
        CoordinatedShutdown(system).run(UnknownReason)
    }
}

object ex1_2 extends App {
    val system = ActorSystem("PingPongSystem")

    val player1 = system.actorOf(Props(new Player(null)), "player1")
    val player2 = system.actorOf(Props(new Player(player1)), "player2")
    val player3 = system.actorOf(Props(new Player(player2)), "player3")
    player1 ! Player.SetNextPlayer(player3)

    player1 ! "ping"

    system.scheduler.scheduleOnce(2.seconds) {
        player1 ! PoisonPill
        player2 ! PoisonPill
        player3 ! PoisonPill
        CoordinatedShutdown(system).run(UnknownReason)
    }
}

object ex1_3 extends App {
    val system = ActorSystem("PingPongSystem")

    val players = (1 to 5).map(i => system.actorOf(Props(new Player(null)), s"player$i")).toList

    players.zip(players.tail :+ players.head).foreach { case (player, nextPlayer) =>
        player ! Player.SetNextPlayer(nextPlayer)
    }

    
    system.scheduler.scheduleOnce(500.milliseconds) {
        players.head ! "ping"
    }

    system.scheduler.scheduleOnce(2.seconds) {
        players.foreach(_ ! PoisonPill)
        CoordinatedShutdown(system).run(UnknownReason)
    }
}