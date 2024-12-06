package lab4

/* 
    Korzystając z metod minBy, maxBy, zdefiniuj funkcję:
        def minMax(seq: Seq[(String, Double)]): Option[(String, String)] = /* ... */
    która zwróci nazwę użytkownika w seq, który zdobył najwięcej i najmniej punktów.
*/

import scala.annotation.tailrec

object ex9 extends App {
    def minMax(seq: Seq[(String, Double)]): Option[(String, String)] = seq match {
        case Nil => None
        case _ => Some(seq.minBy { case (_, res) => res }._1, seq.maxBy { case (_, res) => res }._1)
    }
        

    val seq = Seq(("user1", 5.0), ("user2", 3.0), ("user3", 8.0), ("user4", 7.0))
    println(minMax(seq)) // Output: Seq("user2", "user3")
}
