package lab2

/* 
    Zdefiniuj funkcję value(n: Int): Int, która zwróci n-ty wyrażony wzorem:
    F(0) = 2
    F(1) = 1
    F(n) = F(n-1) + F(n-2) dla n > 1
    Rozwiąż to zadanie bez korzystania ze zmiennych oraz wykorzystaj rekurencję ogonową.
    Pierwsze 10 wyrazów ciągu: 2, 1, 3, 4, 7, 11, 18, 29, 47, 76.
*/

import scala.annotation.tailrec


object ex4 extends App {
    def value(n: Int): Int = {
        @tailrec
        def valueHelper(x: Int, prev1: Int, prev2: Int): Int = {
            if (x == 0) prev1
            else if (x == 1) prev2
            else valueHelper(x - 1, prev2, prev1 + prev2)
        }
        valueHelper(n, 2, 1)
    }

    (0 to 9).foreach { i =>
        println(s"F($i) = ${value(i)}")
    }
}
