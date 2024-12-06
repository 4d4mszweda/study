package lab4

/* 
    Korzystając z metod sortBy, apply, zdefiniuj funkcję:
        def median(seq: Seq[(String, Double)]): Double = /* ... */
    która zwróci medianę wyników znajdujących się w seq, który zawiera nazwy użytkownika i liczby punktów.
*/

import scala.annotation.tailrec

object ex8 extends App {
    def median(seq: Seq[(String, Double)]): Double = {
        val sortedScores = seq.sortBy { case (_, score) => score }.map { case (_, score) => score }

        sortedScores.size % 2 match {
            case 0 => 
                val (left, right) = (sortedScores(sortedScores.size / 2 - 1), sortedScores(sortedScores.size / 2))
                (left + right) / 2
            case 1 => 
                sortedScores(sortedScores.size / 2)
        }
    }

    val seq = Seq(("user1", 5.0), ("user2", 3.0), ("user3", 8.0), ("user4", 7.0))
    println(median(seq)) // Output: 6.0
}
