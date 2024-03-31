fn main() {
    arrays();
}


fn arrays() {
    let a = [1, 2, 3, 4, 5];
    let a2 = [0; 5];
    let a3: [i32; 5] = [1, 2, 3, 4, 5];

    let slice = &a[1..3];
    println!("{:?}", a);
    println!("{:?}", a2);
    println!("{:?}", a3);
    // {:?} is a debug formatter
    println!("{:?}", slice); 
}