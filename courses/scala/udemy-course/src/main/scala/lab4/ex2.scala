package lab4

/* 
    Korzystając z metod filter, map i zipWithIndex, zdefiniuj funkcję:
        def remElems[A](seq: Seq[A], k: Int): Seq[A] = /* ... */
    która usunie k-ty element sekwencji seq.
*/

import scala.annotation.tailrec

object ex2 extends App {
    def remElems[A](seq: Seq[A], k: Int): Seq[A] = seq.zipWithIndex.filter((_, index) => (index + 1) % k != 0).map((elem, _) => elem)

    // case jest potrzebny??
    // seq.zipWithIndex.filter { case (_, index) => (index + 1) % k != 0 }.map { case (elem, _) => elem }

    val seq = Seq(1, 2, 3, 4, 5, 6, 7, 8, 9)
    val k = 3

    println(remElems(seq, k)) // Output: Seq(1, 2, 4, 5, 7, 8)
}
