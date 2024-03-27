use std::env;

#[allow(non_snake_case)]


fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 3 {
        println!("Użycie: cargo run -- <start> <koniec>");
        return;
    }

    let start: usize = match args[1].parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Podana pierwsza wartość nie jest liczbą całkowitą dodatnią.");
            return;
        }
    };

    let end: usize = match args[2].parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Podana druga wartość nie jest liczbą całkowitą dodatnią.");
            return;
        }
    };

    if start > end {
        println!("Pierwsza liczba musi być mniejsza niż druga liczba.");
        return;
    }

    let mut max_num = end;

    let mut table: Vec<Vec<usize>> = vec![vec![0; end - start + 1]; end - start + 1];

    for i in start..=end {
        for j in start..=end {
            table[i - start][j - start] = i * j;
            if table[i - start][j - start] > max_num {
                max_num = table[i - start][j - start];
            }
        }
    }

    let max_entry_width = max_num.to_string().len() + 1;

    print!("{:width$}", "", width = max_entry_width);
    for i in start..=end {
        print!("{:width$}", i, width = max_entry_width);
    }
    println!();

    for i in start..=end {
        print!("{:width$}", i, width = max_entry_width);
        for j in start..=end {
            print!("{:width$}", table[i - start][j - start], width = max_entry_width);
        }
        println!();
    }
}

