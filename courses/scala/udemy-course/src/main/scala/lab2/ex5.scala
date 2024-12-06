package lab2

/* 
    Używając rekurencji ogonowej, zdefiniuj funkcję:
    def isOrdered(tab: Array[Int], mlr: (Int, Int) => Boolean): Boolean
    
    która sprawdza, czy tablica liczb całkowitych będąca jej argumentem jest uporządkowana zgodnie z porządkiem definiowanym przez funkcję mlr.
    Rozwiąż to zadanie bez korzystania ze zmiennych.
    Przykład:
    Dla: tab = Array(1, 3, 3, 6, 8) i mlr = (_ <= _) funkcja powinna zwrócić true.
    Dla: tab = Array(1, 3, 3, 6, 8) i mlr = (_ < _) funkcja powinna zwrócić false
*/

import scala.annotation.tailrec

object ex5 extends App {
    def isOrdered(tab: Array[Int], mlr: (Int, Int) => Boolean): Boolean = {
        @tailrec
        def isOrderedHelper(index: Int): Boolean = {
            if (index >= tab.length - 1) true
            else if (!mlr(tab(index), tab(index + 1))) false
            else isOrderedHelper(index + 1)
        }
        if (tab.isEmpty || tab.length == 1) true
        else isOrderedHelper(0)
    }

    println(isOrdered(tab = Array(1, 3, 3, 6, 8), mlr = (_ <= _)))
    println(isOrdered(tab = Array(1, 3, 3, 6, 8), mlr = (_ < _)))
}
