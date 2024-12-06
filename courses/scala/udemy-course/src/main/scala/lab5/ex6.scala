package lab5

/* 
    Napisz program, który, przy pomocy metod oferowanych przez kolekcję, oblicza wyniki zawodów sportowych w konkurencji, w której zawodnicy oceniani są w dwóch kategoriach:
        wdzięk
        spryt
    Ocena "cząstkowa" ma postać:
        ("Imię", "Nazwisko", ocena_wdzięku, ocena_sprytu)
    Załóż, że:
        zawodnicy identyfikowani są poprzez imię i nazwisko
        każdy zawodnik może otrzymać dowolną liczbę ocen "cząstkowych"
        ocena_wdzięku oraz ocena_sprytu są dowolnymi liczbami całkowitymi z zakresu od 0 do 20.
    Ostateczny wynik zawodnika jest to para liczb typu Double będących średnimi arytmetycznymi ocen cząstkowych w podanych powyżej "kategoriach".
    "Ranking" ustala się sumując obie "średnie" noty każdego z zawodników - wyższa suma oznacza lepszy wynik.
    Jeśli sumy not dwóch zawodników są identyczne, to wyższe miejsce zajmuje ten, którego (średnia) nota za wdzięk była wyższa. Jeśli również noty za wdzięk są identyczne, to zawodnicy zajmują miejsca ex-aequo.
    Załóż, że dane wejściowe programu stanowi lista obiektów reprezentujących oceny "cząstkowe". Program powinien stworzyć uporządkowaną listę obiektów reprezentujących informacje o:
        miejscu zajętym przez zawodnika.
        imieniu i nazwisku zawodnika.
        uzyskanym wyniku.
    W przypadku miejsc ex-aequo kolejność na liście wynikowej powinna być zgodna z porządkiem alfabetycznym nazwisk zawodników.
*/

import scala.annotation.tailrec

object ex6 extends App {
    
}
