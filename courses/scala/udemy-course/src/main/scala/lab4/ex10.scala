package lab4

/* 
    Korzystając z "wyliczenia" for/yield, zdefiniuj funkcję:
        def threeNumbers(n: Int): Set[(Int, Int, Int)] = /* ... */
    która zwróci sekwencję zawierającą wszystkie kombinacje trzech liczb: 
        (a, b, c), liczby a, b, c, są liczbami z przedziału [1, n], które są zgodne ze wzorem:
        a2 + b2 = c2, gdzie a < b.
    Podpowiedź: Sposób wygenerowania ciągu liczb od z przedziału [a, b]: (a to b).toList.
*/

import scala.annotation.tailrec

object ex10 extends App {
    def threeNumbers(n: Int): Set[(Int, Int, Int)] = {
        (for {
            a <- 1 to n
            b <- a + 1 to n
            c <- b + 1 to n
            if a * a + b * b == c * c
        } yield (a, b, c)).toSet
    }

    
    println(threeNumbers(20))
}
