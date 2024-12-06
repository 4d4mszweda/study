package lab3

/* 
    Zdefiniuj generyczną funkcję
    def compute[A, B](l: List[Option[A]])(op1: A => B)(op2: (A, B) => B): Option[B] = /* ... */

    która korzystając z wartości początkowej oraz funkcji op1 (dla pierwszego elementu listy) i op2, obliczy "wartość" ciągu l. 

    Zdefiniuj funkcję z użyciem rekurencji ogonowej.
    Funkcja powinna zwrócić wartość None, wtedy i tylko wtedy, gdy wszystkie elementy listy l, będą miały wartość None.

    W rozwiązaniu skorzystaj z rekurencji ogonowej i dopasowania wzorca (nie używaj metod head i tail).
    Przykład:
    Dla: l = List(Some(1), None, Some(2), None, Some(3), Some(4)), op1 = (_ + 0), op2 = (_ + _), funkcja powinna zwrócić: Some(10).
*/

import scala.annotation.tailrec

object ex5 extends App {
    def compute[A, B](l: List[Option[A]])(op1: A => B)(op2: (A, B) => B): Option[B] = {
        @tailrec
        def computeHandler(l: List[Option[A]], acc: Option[B]): Option[B] = l match {
            case Nil => acc
            case Some(x) :: xs => acc match {
                case None => computeHandler(xs, Some(op1(x)))
                case Some(y) => computeHandler(xs, Some(op2(x, y)))
            }
            case None :: xs => computeHandler(xs, acc)
        }

        computeHandler(l, None)
    }

    val l = List(Some(1), None, Some(2), None, Some(3), Some(4))
    val op1 = (x: Int) => x + 0
    val op2 = (x: Int, y: Int) => x + y

    println(compute(l)(op1)(op2)) // Output: Some(10)
}
