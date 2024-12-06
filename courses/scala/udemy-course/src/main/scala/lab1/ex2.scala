package lab1

/*
    Zdefiniuj klasę C, która będzie reprezentowała liczby zespolone.
    klasa powinna zawierać pola re i im reprezentujące część rzeczywistą i urojoną liczby.
    zdefiniuj odpowiednie konstruktory
        konstruktor główny: dzięki któremu, będzie można przypisać wartości części rzeczywistej i urojonej, tworząc obiekt.
        konstruktor pomocniczy: dzięki któremu, będzie można przypisać jedynie wartość części rzeczywistej, tworząc obiekt.

    reprezentacja tekstowa obiektów klasy, powinna być bardziej czytelna:
        dla b>0: a + bi
        dla b<0: a – bi
        dla b=0: a

    powinna zawierać metody:
        +(that: C): C
        -(that: C): C
        *(that: C): C
    które umożliwią wykonanie operacji arytmetycznych na liczbach zespolonych.

    powinna zawierać metodę:
        /(that: C): C
    która umożliwi wykonanie operacji arytmetycznej na liczbach zespolonych.
    jeżeli podany argument będzie powodował dzielenie przez 0, powinien zostać uruchomiony wyjątek IllegalArgumentException. wywołaj metodę i obsłuż odpowiednio wyjątek.
    obiekty klasy, powinny mieć możliwość wykonywania operacji arytmetycznych ze w zwykłymi liczbami rzeczywistymi.

    Przykładowo powinny działać operacje:
        5.3 + C(2.1, 3.5)
        C(2.2, 3.4) * 2.5

    obiekty klasy, powinny mieć możliwość wykonywania operatorów logicznych: ==, !=, <, >, <=, >= na liczbach zespolonych.
    przyjmij, że operatory są zgodne z odległością od współrzędnej (0, 0) na osi Re, Im.
    wykorzystaj cechę Ordered[A], albo metodę equals, tam gdzie to możliwe.
*/

class C(val re: Double, val im: Double) {
    def this(re: Double) = this(re, 0.0)

    override def toString: String = im match {
        case 0 => s"$re"
        case _ if im > 0 => s"$re + ${im}i"
        case _ => s"$re - ${-im}i"
    }

    def +(that: C): C = new C(this.re + that.re, this.im + that.im)
    def -(that: C): C = new C(this.re - that.re, this.im - that.im)
    def *(that: C): C = new C(this.re * that.re - this.im * that.im, this.re * that.im + this.im * that.re)
    def /(that: C): C = {
        val denom = that.re * that.re + that.im * that.im
        if (denom == 0) throw new IllegalArgumentException("Division by zero")
        new C((this.re * that.re + this.im * that.im) / denom, (this.im * that.re - this.re * that.im) / denom)
    }

    override def equals(obj: Any): Boolean = obj match {
        case that: C => this.re == that.re && this.im == that.im
        case _ => false
    }

    def ==(that: C): Boolean = this.equals(that)
    def !=(that: C): Boolean = !this.equals(that)
    def <(that: C): Boolean = this.magnitude < that.magnitude
    def >(that: C): Boolean = this.magnitude > that.magnitude
    def <=(that: C): Boolean = this.magnitude <= that.magnitude
    def >=(that: C): Boolean = this.magnitude >= that.magnitude

    private def magnitude: Double = Math.sqrt(re * re + im * im)
}

object ex2 extends App {
    val c1 = new C(2.1, 3.5)
    val c2 = new C(2.1)
    println(c1)
    println(c2)
    println(c1 + c2)
    println(c1 - c2)
    println(c1 * c2)
    try {
        println(c1 / new C(0, 0))
    } catch {
        case e: IllegalArgumentException => println(e.getMessage)
    }
}
