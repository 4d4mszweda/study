package lab3

/* 
    Zdefiniuj generyczną funkcję
    def isSub[A](l: List[A], lSub: List[A]): Boolean = /* ... */

    która zwróci informację czy wszystkie elementy w lSub znajdują się w l. Możesz założyć, że elementy w lSub są unikatowe.
    W rozwiązaniu skorzystaj z rekurencji ogonowej i dopasowania wzorca (nie używaj metod head i tail).

    Przykład:
    Dla lSub = List('a', 'b', 'c') i l = List('b', 'o', 'c', 'i', 'a', 'n'), powinna zostać zwrócona true.
*/

import scala.annotation.tailrec

object ex4 extends App {
    def isSub[A](l: List[A], lSub: List[A]): Boolean = {
        @tailrec
        def isSubHelper(curr: List[A]): Boolean = curr match {
            case Nil => true
            case xh :: xt => if (l.contains(xh)) isSubHelper(xt) else false
        }

        isSubHelper(lSub)
    }
    

    val l = List('b', 'o', 'c', 'i', 'a', 'n')
    val lSub = List('a', 'b', 'c')

    println(isSub(l, lSub)) // Output: true
}
