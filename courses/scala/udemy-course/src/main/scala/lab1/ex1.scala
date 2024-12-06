package lab1

/*  
    Napisz program, który pobierze od użytkownika liczbę n oraz wyświetli informację, 
    czy każda naturalna liczba parzysta większa od 2 i mniejsza równa od n – liczby z przedziału (2, n] jest sumą dwóch liczb pierwszych.
    Dodatkowo na ekranie powinny zostać wypisane wszystkie te podziały.
    Przykład:
    Liczba: 8
    Liczba jest sumą: 3+5=8
*/

import scala.annotation.tailrec

object ex1 extends App {
    val num: Int = 20 // powiedzmy że pobranie
    val primeNumbers: Seq[Int] = (3 to num).filter(isPrime)
    
    
    def isPrime(n: Int): Boolean = {
        @tailrec
        def isPrimeHelper(t: Int): Boolean = if (t <= 1) true else n % t != 0 && isPrimeHelper(t - 1)
        if (n <= 1) false else isPrimeHelper(n / 2)
    }

    def isSumOfTwoPrimes(even: Int): Boolean = {
        primeNumbers.exists(p => primeNumbers.contains(even - p))
    }

    (4 to num by 2).foreach { even =>
        val pairs = for {
            p1 <- primeNumbers
            p2 <- primeNumbers
            if p1 + p2 == even
        } yield s"$p1+$p2=$even"
        
        if (pairs.nonEmpty) {
            println(s"Liczba $even jest sumą: ${pairs.mkString(", ")}")
        } else {
            println(s"Liczba $even nie jest sumą dwóch liczb pierwszych")
        }
    }
}
