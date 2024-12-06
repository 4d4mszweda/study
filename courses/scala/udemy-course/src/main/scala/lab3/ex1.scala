package lab3

/* 
    Napisz generyczną funkcję
    def divide[A](list: List[A]): (List[A], List[A]) = /* ... */

    która podzieli listę list na dwie części. W pierwszej będą się znajdywać elementy na parzystych indeksach w drugiej elementy na nieparzystych.
    Przykład:
    divide(List(1, 3, 5, 6, 7)) == (List(1, 5, 7), List(3, 6))

    W rozwiązaniu skorzystaj z rekurencji ogonowej i dopasowania wzorca (nie używaj metod head i tail).
*/

import scala.annotation.tailrec

object ex1 extends App {
    def divide[A](list: List[A]): (List[A], List[A]) = {
        @tailrec
        def divideHelper(remaining: List[A], list1: List[A], list2: List[A], isEven: Boolean): (List[A], List[A]) = remaining match {
            case Nil => (list1.reverse, list2.reverse)
            case x :: xs =>
                if (isEven) divideHelper(xs, x :: list1, list2, !isEven)
                else divideHelper(xs, list1, x :: list2, !isEven)
        }

        divideHelper(list, List(), List(), true)
    }


    println(divide(List(1, 3, 5, 6, 7)))
}
