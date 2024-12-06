package lab2

/* 
    Zdefiniuj funkcję rekurencyjną ogonowo:
    def worth(tab1: Array[Int], tab2: Array[Int])(pred: (Int, Int) => Boolean)(op: (Int, Int) => Int): Option[Int]

    która zwróci wartość zwracaną przez op, dla pierwszych wartości, 
    które znajdują się na tych samych pozycjach tablic oraz spełniają predykat pred. 
    Jeżeli takie wartości nie istnieją, powinna zostać zwrócona wartość None.
    Rozwiąż to zadanie bez korzystania ze zmiennych.

    Przykład:
    Dla: tab1 = Array(-1, 3, 2, -8, 5) , tab2 = Array(-3, 3, 3, 0, -4, 5) , pred = (_ < _) , op = (_ + _) , funkcja powinna zwrócić Some(5), ponieważ
    -1 < -3 // fałsz, pomijamy
    3 < 3 // fałsz, pomijamy
    2 < 3 // prawda, zwracamy Some(5), ponieważ 2 + 3 = 5
*/

import scala.annotation.tailrec

object ex6 extends App {
    def worth(tab1: Array[Int], tab2: Array[Int])(pred: (Int, Int) => Boolean)(op: (Int, Int) => Int): Option[Int] = {
        @tailrec
        def worthHelper(index: Int): Option[Int] = {
            if (index >= tab1.length-1 || index >= tab2.length-1) None
            else if(pred(tab1(index), tab2(index))) Some(op(tab1(index), tab2(index)))
            else worthHelper(index+1)
        }
        worthHelper(0)
    }

    val tab1 = Array(-1, 3, 2, -8, 5)
    val tab2 = Array(-3, 3, 3, 0, -4, 5)
    val pred = (a: Int, b: Int) => a < b
    val op = (a: Int, b: Int) => a + b

    val result = worth(tab1, tab2)(pred)(op)
    println(result) // Powinno zwrócić Some(5)
}
