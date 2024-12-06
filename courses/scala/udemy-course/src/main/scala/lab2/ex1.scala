package lab2

/* 
    Zdefiniuj funkcję reverse(str: String): String, która zwróci odwrócony napis pobrany jako argument.
    Rozwiąż to zadanie bez korzystania ze zmiennych oraz wykorzystaj rekurencję ogonową.
*/

import scala.annotation.tailrec

object ex1 extends App {
    def reverse(str: String): String = {
        @tailrec
        def reverseHelper(str: String, acc: String = ""): String = if (str.isEmpty()) acc else reverseHelper(str.tail, str.head + acc)
        reverseHelper(str)
    }

    println(reverse("Ala ma kota"))
}
