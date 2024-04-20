package main

import "fmt"

// type Product struct {
// 	id int
// 	name string
// 	price float64
// }

func main() {
	prices := []float64{1.1, 2.2, 3.3, 4.4, 5.5}

	// slice
	fmt.Println(prices[1:3])
	fmt.Println(prices[:3])
	fmt.Println(prices[1:])

	fmt.Println(len(prices))

	fmt.Println(cap(prices))

	// for each loop
	for i, price := range prices {
		fmt.Println(i, price)
	}

	// map
	newPrices := []float64{25.1, 36.2, 19.3, 46.4, 46.5}
	prices = append(prices, newPrices...)
	fmt.Println(prices)

	maps()

	var cos = [2]string{}
	cos[0] = "cos1"
	cos[1] = "cos2"
	fmt.Println(cos)


	// make creates a slice with a length and capacity fill of 0
	var makeExample = make([]int, 5, 10)
	fmt.Println(makeExample)
}


func maps(){
	website := map[string]string{"site": "golang.org", "language": "Go"}
	fmt.Println(website)
	fmt.Println(website["site"])
	fmt.Println(website["language"])

	website["site"] = "golang.com"
	fmt.Println(website)

	delete(website, "site")
	fmt.Println(website)
}