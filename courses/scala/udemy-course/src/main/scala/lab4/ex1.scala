package lab4

/* 
    Korzystając z metod drop i take, zdefiniuj funkcję:
        def subSeq[A](seq: Seq[A], begIdx: Int, endIdx: Int): Seq[A] = /* ... */
    która zwraca podciąg ciągów sekwencji seq z przedziału od indeksu begIdx do endIdx.
*/

import scala.annotation.tailrec

object ex1 extends App {
    def subSeq[A](seq: Seq[A], begIdx: Int, endIdx: Int): Seq[A] = seq.drop(begIdx).take(endIdx - begIdx + 1)

    val seq = Seq(1, 2, 3, 4, 5, 6, 7, 8, 9)
    val begIdx = 2
    val endIdx = 5

    println(subSeq(seq, begIdx, endIdx)) // Output: Seq(3, 4, 5, 6)
}
