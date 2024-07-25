use std::io::{self, BufRead};
pub fn benford() {
    let mut hista = [0u64; 10];
    let stdin = io::stdin();
    let reader = stdin.lock();
    for line in reader.lines() {
        match line {
            Ok(line) => {
                for word in line.split_whitespace(){
                    for digit in word.as_bytes(){
                        let cyfra = (*digit - 48) as usize;
                        hista[cyfra] += 1;
                    }
                }
            }
            Err(error) => {
                eprintln!("error: {}", error);
                std::process::exit(1);
            }
        }
    }

    for (i, h) in hista.iter().enumerate() {
        println!("{} {}", i, *h);
    }
}