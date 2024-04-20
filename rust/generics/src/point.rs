pub struct Point {
    pub x : i32,
    pub y : i32,
}

impl Point {
    pub fn new(x: i32, y: i32) -> Self {
        Self { x, y}
    }
}

#[cfg(test)]

mod test{
    #[test]
    fn test_new(){
        let p = Point::new(1, 2);
        assert_eq!(p.x, 1);
        assert_eq!(p.y, 2);
    }
}