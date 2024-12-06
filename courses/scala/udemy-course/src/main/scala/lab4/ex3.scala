package lab4

/* 
    Korzystając z metody zip i innych metod, zdefiniuj funkcję:
        def diff[A](seq1: Seq[A], seq2: Seq[A]): Seq[A] = /* ... */
    która zwróci wszystkie elementy z seq1, które nie pasują wg "indeksów" z seq2.
    Przykład:
    Dla: seq1 = Seq(1, 2, 3), seq2 = Seq(2, 2, 1, 3), funkcja powinna zwrócić: Seq(1, 3), ponieważ
        seq1(0) != seq2(0) // zostawiamy
        seq1(1) == seq2(1) // usuwamy
        seq1(2) != seq2(2) // zostawiamy
*/

import scala.annotation.tailrec

object ex3 extends App {
    def diff[A](seq1: Seq[A], seq2: Seq[A]): Seq[A] = seq1.zip(seq2).filter((x, y) => x != y).map((x,_)=> x)

    def diff2[A](seq1: Seq[A], seq2: Seq[A]): Seq[A] = {
        seq1.zip(seq2).filter { case (x, y) => x != y }.map { case (x, _) => x } ++ seq1.drop(seq2.length)
    }
    
    println(diff(Seq(1, 2, 3), seq2 = Seq(2, 2, 1, 3)))
    println(diff2(Seq(1, 2, 3), seq2 = Seq(2, 2, 1, 3)))
}
