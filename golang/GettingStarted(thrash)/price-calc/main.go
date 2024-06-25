package main

import (
	"example.com/price-calc/prices"
)

func main() {
	taxRates := []float64{0, 0.07, 0.1, 0.15}
	
	for _, taxtaxRate := range taxRates {
		priceJob := prices.NewTaxIncludedPriceJob(taxtaxRate)
		priceJob.Process()
	}
	}