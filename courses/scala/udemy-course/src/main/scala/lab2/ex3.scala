package lab2

/* 
    Zdefiniuj funkcję binToDec(bin: Int): Int, która jako argument otrzyma liczbę zapisaną w systemie binarnym i przeliczy ją na system dziesiętny. 
    Rozwiąż to zadanie bez korzystania ze zmiennych oraz wykorzystaj rekurencję ogonową.
*/

import scala.annotation.tailrec


object ex3 extends App {
  def binToDec(bin: Int): Int = {
    @tailrec
    def binToDecHelper(binary: Int, acc: Int, power: Int): Int = 
        if (binary == 0) acc 
        else binToDecHelper(binary / 10, acc + (binary % 10) * Math.pow(2, power).toInt, power + 1)
    binToDecHelper(bin, 0, 0)
  }
}
