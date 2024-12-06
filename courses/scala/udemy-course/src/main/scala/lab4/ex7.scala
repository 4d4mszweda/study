package lab4

/* 
    Korzystając z metody groupBy i innych metod, zdefiniuj funkcję:
        def freq[A](seq: Seq[A]): Set[(A, Int)] = /* ... */
    która zwróci częstość wystąpienia poszczególnych elementów w ciągu seq.
    Przykład:
    Dla: seq = Seq('a','b','a','c','c','a') funkcja powinna zwrócić Set(('a', 3),('b', 1),('c', 2)).
*/

import scala.annotation.tailrec

object ex7 extends App {
    def freq[A](seq: Seq[A]): Set[(A, Int)] = 
        seq.groupBy(identity).map { case (elem, occurrences) => (elem, occurrences.size) }.toSet
    
    println(freq(Seq('a','b','a','c','c','a')))
}
