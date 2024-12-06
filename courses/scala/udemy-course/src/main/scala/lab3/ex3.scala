package lab3

/* 
    Napisz generyczną funkcję
    def compress[A](list: List[A]): List[(A, Int)]

    która w liście list zastępuje każdy podciąg powtarzających się elementów a...a parą (a, długość podciągu).
    W rozwiązaniu skorzystaj z rekurencji ogonowej i dopasowania wzorca (nie używaj metod head i tail).
    Przykład:
    compress(List('a','a','b','c','c','c','d','d','c')) == List( ('a',2), ('b',1), ('c',3), ('d',2), ('c',1) )
*/

import scala.annotation.tailrec

object ex3 extends App {
    def compress[A](list: List[A]): List[(A, Int)] = {
        @tailrec
        def compressHelper(remaining: List[A], current: Option[(A, Int)], acc: List[(A, Int)]): List[(A, Int)] = remaining match {
            case Nil => current match {
                case Some((elem, count)) => (elem, count) :: acc
                case None => acc
            }
            case x :: xs => current match {
                case Some((elem, count)) if elem == x => compressHelper(xs, Some((elem, count + 1)), acc)
                case Some((elem, count)) => compressHelper(xs, Some((x, 1)), (elem, count) :: acc)
                case None => compressHelper(xs, Some((x, 1)), acc)
            }
        }

        compressHelper(list, None, Nil).reverse
    }
    
    println(compress(List('a', 'a', 'b', 'c', 'c', 'c', 'd', 'd', 'c'))) // Output: List(('a',2), ('b',1), ('c',3), ('d',2), ('c',1))
}
