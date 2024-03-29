// Every Go program is made up of packages. Programs start running in package main.
package main

// fmt is a package that provides I/O functions. Its name is short for "format".
// Its part of the Go standard library.
import "fmt"

// Global variables. They are declared outside of any function.
const PI = 3.14


// The main function is where the program starts running. Its a special function.
func main() {
	i_o_example()
	x, y := returnExample(1, 2)
	fmt.Println(x, y)
}

func i_o_example() {
	var ravenue, expenses int
	var taxRate float64

	fmt.Print("Enter ravenue: ")
	// Scan is a function in the fmt package that reads user input from the console.
	// It takes a pointer to the variable where the input should be stored.
	fmt.Scan(&ravenue)
	fmt.Print("Enter expenses: ")
	fmt.Scan(&expenses)
	fmt.Print("Enter tax rate: ")
	fmt.Scan(&taxRate)

	// Its a second way to declare variables. The := syntax is shorthand for declaring and initializing a variable.
	ebt := ravenue - expenses
	profit := float64(ebt) * (1 - taxRate/100)
	ratio := profit / float64(ravenue)

	// Println is a function in the fmt package that outputs a line to the console.
	// Printf is a function in the fmt package that allows us to format the output.
	fmt.Printf("Earnings before tax: %v\n", ebt)
	fmt.Println("Profit: ", profit)
	fmt.Println("Profit ratio: ", ratio)

	// Print with 2 decimal places. Just like in Python.
	fmt.Printf("Earnings before tax: %.2f\n", ratio)

	// Print type of variable.
	fmt.Printf("%T\n", ravenue)
	// ` ` used like in JS for multiline strings.
	fmt.Printf(`cos
	cos 2 `)
}

//return many values
func returnExample(x, y float64) (float64, float64) {
	z := x + y
	w := x - y
	return z, w
}

// Named return values. It's a way to declare the return values at the beginning of the function.
// func returnExample(x, y float64) (z float64, w float64) {
// 	z = x + y
// 	w = x - y
// 	return
// }
