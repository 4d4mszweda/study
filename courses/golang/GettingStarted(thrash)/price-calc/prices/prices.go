package prices

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"

	"example.com/price-calc/conversion"
)

type TaxIncludedPriceJob struct {
	TaxRate float64	`json:"tax_rate"`
	Prices  []float64 `json:"prices"`
	TaxIncludedPrices map[string]float64 `json:"tax_included_prices"`
}

func (job *TaxIncludedPriceJob) LoadData() {
	file, err := os.Open("prices.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	scanner := bufio.NewScanner(file)

	var lines []string
	
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	err = scanner.Err()
	if err != nil {
		fmt.Println(err)
		file.Close()
		return
	}

	prices, err := conversion.StringsToFloats(lines)
	if err != nil {
		fmt.Println(err)
		file.Close()
		return
	}
	job.Prices = prices
	file.Close()
}

func (job TaxIncludedPriceJob) Process() {
	job.LoadData()
	result := make(map[string]float64)
	for _, price := range job.Prices {
		job.TaxIncludedPrices[fmt.Sprintf("%.2f", price)] = price * (1 + job.TaxRate)
		result[fmt.Sprintf("%.2f", price)] = price * (1 + job.TaxRate)
	}	

	job.TaxIncludedPrices = result
	err := WriteToJson("tax_included_prices.json", job)
	if err != nil {
		fmt.Println(err)
	}
}

func NewTaxIncludedPriceJob(taxRate float64) *TaxIncludedPriceJob {
	return &TaxIncludedPriceJob{
		TaxRate: taxRate,
		Prices: []float64{10, 20, 30},
		TaxIncludedPrices: make(map[string]float64),
	}
}

func WriteToJson(path string, data interface{}) error {
	file, err := os.Create(path)
	if err != nil {
		fmt.Println(err)
		return err
	}
	err = json.NewEncoder(file).Encode(data)
	if err != nil {
		fmt.Println(err)
		return err
	}
	return nil
}