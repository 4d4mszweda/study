package lab4

/* 
    Korzystając z metody sliding i innych metod, zdefiniuj funkcję:
        def isOrdered[A](seq: Seq[A])(leq:(A, A) => Boolean): Boolean = /* ... */
    która zwróci informację czy wszystkie sąsiednie elementy w seq, są zgodne z predykatem leq.
    Przykłady:
    Dla: seq = Seq(1, 2, 2, 4) i leq = (_ < _) funkcja powinna zwrócić false.
    Dla: seq = Seq(1, 2, 2, 4) i leq = (_ <= _) funkcja powinna zwrócić true.
*/

import scala.annotation.tailrec

object ex6 extends App {
    def isOrdered[A](seq: Seq[A])(leq:(A, A) => Boolean): Boolean = seq.sliding(2).forall {
        case Seq(a, b) => leq(a, b)
        case _ => true
    }
    
    val seq1 = Seq(1, 2, 2, 4)
    val leq1 = (x: Int, y: Int) => x < y
    println(isOrdered(seq1)(leq1)) // Output: false

    val seq2 = Seq(1, 2, 2, 4)
    val leq2 = (x: Int, y: Int) => x <= y
    println(isOrdered(seq2)(leq2)) // Output: true
}
