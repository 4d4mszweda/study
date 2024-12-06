package lab4

/* 
    Korzystając z metody foldLeft/foldRight, zdefiniuj generyczną funkcję:
        def deStutter[A](seq: Seq[A]): Seq[A] = /* ... */
    która usunie z sekwencji seq wszystkie powtarzające się ciągi.
    Przykład:
    Dla: seq = Seq(1, 1, 2, 4, 4, 4, 1, 3), funkcja powinna zwrócić: Seq(1, 2, 4, 1, 3).
*/

import scala.annotation.tailrec

object ex5 extends App {
    def deStutter[A](seq: Seq[A]): Seq[A] = seq.foldLeft(Seq.empty[A]) {
        case (acc, elem) if acc.isEmpty || acc.last != elem => acc :+ elem
        case (acc, _) => acc
    }

    println(deStutter(Seq(1, 1, 2, 4, 4, 4, 1, 3)))
}
