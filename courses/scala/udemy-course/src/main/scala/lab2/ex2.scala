package lab2

/* 
    Zdefiniuj funkcję isPrime(n: Int): Boolean która sprawdza, czy argument jest liczba pierwszą. 
    Rozwiąż to zadanie bez korzystania ze zmiennych oraz wykorzystaj rekurencję ogonową.
*/

import scala.annotation.tailrec


object ex2 extends App {
    def isPrime(n: Int): Boolean = {
        @tailrec
        def isPrimeHelper(t: Int): Boolean = if (t <= 1) true else n % t != 0 && isPrimeHelper(t - 1)
        if (n <= 1) false else isPrimeHelper(n / 2)
    }

    println(isPrime(7))
    println(isPrime(8))
}
