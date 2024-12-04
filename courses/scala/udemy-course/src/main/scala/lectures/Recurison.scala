package lectures

import scala.annotation.tailrec

object Recurison extends App {
    def factorial(n: BigInt) :BigInt = 
        if n == 1 then n 
        else n * factorial(n - 1)


        // Aby rekurencja była ogona to wywołanie rekurencyjne musi być ostatnim wywołaniem
    def tailFactorial(n: BigInt): BigInt = {
        @tailrec
        def factorialHelper(n: BigInt, acc: BigInt): BigInt =
            if (n <= 1) acc
            else factorialHelper(n-1, n * acc)

        factorialHelper(n, 1)
    }

    println(tailFactorial(5))

    @tailrec
    def concateNTimes(x: String, n: Int, acc: String): String = if (n <= 0) acc else concateNTimes(x, n-1, acc + x)
    println(concateNTimes("Dupa", 5, ""))

    def isPrime(n: Int): Boolean = {
        def isPrimeHelper(t: Int): Boolean = if (t<=1) true else n % t != 0 && isPrimeHelper(t - 1)

        isPrimeHelper(n / 2)
    }
    println(isPrime(27))

    def fibonachi(n: Int) :Int = if n <= 1 then 1 else fibonachi(n-1) + fibonachi(n-2)
    println(fibonachi(8))
}
