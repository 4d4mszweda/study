package lab4

/* 
    Korzystając z metody foldLeft/foldRight, zdefiniuj funkcję:
        def sumOption(seq: Seq[Option[Double]]): Double = /* ... */
    która zwróci sumę elementów sekwencji seq. Wszystkie elementy None powinny zostać pominięte.
    Przykład:
    Dla: seq = Seq(Some(5.4), Some(-2.0), Some(1.0), None, Some(2.6)), funkcja powinna zwrócić: 7.0.
*/

import scala.annotation.tailrec

object ex4 extends App {
    def sumOption(seq: Seq[Option[Double]]): Double = seq.foldLeft(0.0) { 
        case (acc, Some(value)) => acc + value
        case (acc, None) => acc
    }

    println(sumOption(Seq(Some(5.4), Some(-2.0), Some(1.0), None, Some(2.6))))
}
