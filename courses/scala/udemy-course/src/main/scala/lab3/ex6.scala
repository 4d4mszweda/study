package lab3

/* 
    Zapoznaj się z możliwością zwracania funkcji, przez funkcję.

    Zdefiniuj następujące generyczne operujące na funkcjach:
        składanie funkcji:
            def compose[A, B, C](f: A => B)(g: B => C): A => C = /* ... */
        iloczyn funkcji:
            def prod[A, B, C, D](f: A => C, g: B => D): (A, B) => (C, D) = /* ... */
        podniesienie operatora op: (T, T) => T
            def lift[A, B, T](op: (T,T) => T)(f: A => T, g: B => T): (A,B) => T = /* ... */
    Niech MSet[A] oznacza multi-zbiór (zbiór w którym elementy mogą się powtarzać) typu A.
        type MSet[A] = A => Int
    Czyli jest to funkcja zwracająca liczbę wystąpienia elementu typu A w danym multizbiorze. np.
        val s: MSet[Int] = (n: Int) => n match {
            case 1 => 2
            case 3 => 1
            case _ => 0
        }.

    Korzystając z funkcji w podpunkcie a zdefiniuj funkcję wykonujące operację: sumy, różnicy oraz części wspólnej dla wielozbiorów:
        def sum[A](s1: MSet[A], s2: MSet[A]): MSet[A] = /* ... */
        def diff[A](s1: MSet[A], s2: MSet[A]): MSet[A] = /* ... */
        def mult[A](s1: MSet[A], s2: MSet[A]): MSet[A] = /* ... */
*/

import scala.annotation.tailrec

object ex6 extends App {
    def compose[A, B, C](f: A => B)(g: B => C): A => C = {a => g(f(a))}
    def prod[A, B, C, D](f: A => C, g: B => D): (A, B) => (C, D) = {(a, b) => (f(a), g(b))}
    def lift[A, B, T](op: (T,T) => T)(f: A => T, g: B => T): (A,B) => T = {(a, b) => op(f(a), g(b))}

    type MSet[A] = A => Int


    def sum[A](s1: MSet[A], s2: MSet[A]): MSet[A] = {
        a => s1(a) + s2(a)
    }

    def diff[A](s1: MSet[A], s2: MSet[A]): MSet[A] = {
        a => s1(a) - s2(a)
    }

    def mult[A](s1: MSet[A], s2: MSet[A]): MSet[A] = {
        a => Math.min(s1(a), s2(a))
    }

    val s: MSet[Int] = (n: Int) => n match {
        case 1 => 2
        case 3 => 1
        case _ => 0
    }

    val t: MSet[Int] = (n: Int) => n match {
        case 1 => 1
        case 2 => 2
        case _ => 0
    }

    println(sum(s, t)(1)) // Output: 3
    println(diff(s, t)(1)) // Output: 1
    println(mult(s, t)(1)) // Output: 1
}
