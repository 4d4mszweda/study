package main

func main() {
	// Declare a variable of type int
	var a int

	// Declare a pointer to an int
	var p *int

	// Assign the address of a to p
	p = &a

	// Assign a value to a
	a = 42

	// Dereference the pointer to get the value of a
	println(*p) // 42

	// Assign a value to a through the pointer
	*p = 27

	// Get the value of a
	println(a) // 27
}