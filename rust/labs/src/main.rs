mod collatz_conjecture;
mod benford;
use collatz_conjecture::collatz_conjecture;
use benford::benford;

#[allow(non_snake_case)]

fn main() {
    // let N = std::env::args()
    // .nth(1)
    // .expect("Podaj argument")
    // .parse::<u64>()
    // .expect("Podaj liczbę całkowitą");
    println!("\nWitaj oto program obliczający hipotezę Collatza! \n");
    for n in 0 .. 8 {
        collatz_conjecture(n);
    }
    println!("\nWitaj oto program obliczający Benforda! \n");
}
