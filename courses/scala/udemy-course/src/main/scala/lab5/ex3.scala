package lab5

/* 
    Gra MasterMind polega na odgadnięciu w jakich miejscach zostały umieszczone n ukrytych kul, które są oznaczone powtarzającymi się kolorami. Gracz wygrywa, jeżeli w określonej liczbie ruchów odgadnie w jakich miejscach zostały umieszczone kule. W każdej turze gracz wybiera n kul, po czym zostaje mu wyświetlona informacja czy trafił. Każda prawidłowo odgadnięta kula (kula o właściwym kolorze na właściwym miejscu) sygnalizowana jest czarną kropką. Natomiast jeżeli gracz odgadł kolor kuli, ale nie odgadł jej lokalizacji, jest to sygnalizowane białą kropką. Gracz nie wie, które kule są właściwe, które zaś nie.
    Korzystając z funkcji kolekcji zdefiniuj funkcję:
        def score(code: Seq[Int])(move: Seq[Int]): (Int, Int)
    która ocenia ruchy dla gry MasterMind, czyli zwracającą liczbę czarnych i białych kropek.
    Przykładowo, dla:
        val code = Seq(1, 3, 2, 2, 4, 5)
        val move = Seq(2, 1, 2, 4, 7, 2)
    Funkcja powinna zwrócić: (1, 3).
*/

import scala.annotation.tailrec

object ex3 extends App {
    
}
