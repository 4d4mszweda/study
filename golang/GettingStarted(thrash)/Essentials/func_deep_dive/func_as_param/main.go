package func_as_param

import "fmt"

type transformTypeFn func(int) int

func main() {
	numbers := []int{1, 2, 3, 4, 5}
	smt := transformNumbers(&numbers, doubleNumber)
	fmt.Println(numbers)
	fmt.Println(smt)
	smt2 := transformNumbers(&numbers, tripleNumber)
	fmt.Println(smt2)
	smt3 := transformNumbers(&numbers, getTransofrmer("double"))
	fmt.Println(smt3)
}

func transformNumbers(numbers *[]int, transform transformTypeFn) []int {
	nNumbers := []int{}
	for _, n := range *numbers {
		nNumbers = append(nNumbers, transform(n))
	}
	return nNumbers
}

func getTransofrmer(transformType string) transformTypeFn {
	if transformType == "double" {
		return doubleNumber
	}
	return tripleNumber
}

func doubleNumber(number int) int {
	return number * 2
}

func tripleNumber(number int) int {
	return number * 3
}