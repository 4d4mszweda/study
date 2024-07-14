pub fn collatz_conjecture(n: u64) {
    let mut n = n;
    while n > 1 {
        print!("{} ", n);
        if n % 2 == 0 {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
    }
    println!("1");
}