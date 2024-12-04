package lectures

object Functions extends App {
    def aFunction(a: String, b: Int): String = 
        a + " " + b

    // println(aFunction("Cosik", 4))

    def aReapetedFunction(aString: String, n: Int): String = {
        if n == 1 then aString else aString + aReapetedFunction(aString, n - 1)
    }

    // WHEN YOU NEED LOOPS USE RECURSION INSTEED
    // println(aReapetedFunction("jebac", 5))

    def factorial(n: BigInt) :BigInt = if n == 1 then n else n * factorial(n - 1)
    println(factorial(4))
    
    def fibonachi(n: Int) :Int = if n <= 1 then 1 else fibonachi(n-1) + fibonachi(n-2)
    println(fibonachi(8))

    def isPrime(n: Int): Boolean = {
        def isPrimeHelper(t: Int): Boolean = if (t<=1) true else n % t != 0 && isPrimeHelper(t - 1)

        isPrimeHelper(n / 2)
    }

    println(isPrime(27))

    
}
