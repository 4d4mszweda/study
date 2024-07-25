package main

import "fmt"

func main() {
	numbers := []int{1, 2, 3}

	// anonymous function
	transformed := transformNumbers(&numbers, func(n int) int{return n * 2})

	fmt.Println(transformed)

	sum := sumup(numbers)
	fmt.Println(sum)

	sum = sumupVariadic(numbers...)
	fmt.Println(sum)
}

func transformNumbers(numbers *[]int, transform func(int) int) []int {
	dNumbers := []int{}

	for _, val := range *numbers {
		dNumbers = append(dNumbers, transform(val))
	}

	return dNumbers
}

func sumup(numbers []int) int {
	sum := 0

	for _, val := range numbers {
		sum += val
	}

	return sum
}

func sumupVariadic(numbers ...int) int {
	sum := 0

	for _, val := range numbers {
		sum += val
	}

	return sum
}

// Closure its more like a function factory
func createTransformer(n int) func(int) int {
	return func(i int) int {
		return i * n
	}
}