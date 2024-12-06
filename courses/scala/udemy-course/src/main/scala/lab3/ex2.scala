package lab3

/* 
    Zdefiniuj generyczną funkcję
    def merge[A](a: List[A], b: List[A])(leq: (A, A) => Boolean): List[A]

    która połączy ze sobą dowolne dwa ciągi elementów typu A, zgodnie z porządkiem zadanym przez funkcję leq (załóżmy, że ciągi są posortowane).
    W rozwiązaniu skorzystaj z rekurencji ogonowej i dopasowania wzorca (nie używaj metod head i tail).
    Przykład:
    Dla: a = List(1 ,3, 5, 8), b = List(2, 4, 6, 8, 10, 12) i leq = (m, n) => m < n, funkcja powinna zwrócić List(1, 2, 3, 4, 5, 6, 8, 8, 10, 12).
*/

import scala.annotation.tailrec


object ex2 extends App {
    def merge[A](a: List[A], b: List[A])(leq: (A, A) => Boolean): List[A] = {
        @tailrec
        def mergeHelper(a: List[A], b: List[A], acc: List[A]): List[A] = (a, b) match {
            case (Nil, Nil) => acc.reverse
            case (Nil, _) => acc.reverse ++ b
            case (_, Nil) => acc.reverse ++ a
            case (ah :: at, bh :: bt) =>
                if (leq(ah, bh)) mergeHelper(at, b, ah :: acc)
                else mergeHelper(a, bt, bh :: acc)
        }

        mergeHelper(a, b, Nil)
    }
    

    val a = List(1, 3, 5, 8)
    val b = List(2, 4, 6, 8, 10, 12)
    val leq = (m: Int, n: Int) => m < n

    println(merge(a, b)(leq)) // Output: List(1, 2, 3, 4, 5, 6, 8, 8, 10, 12)
}
