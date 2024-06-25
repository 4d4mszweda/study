package conversion

import (
	"strconv"
)

func StringsToFloats(strings []string) ([]float64, error) {
	prices := make([]float64, len(strings))

	for lineIndex, line := range strings {
		floatPrice, err := strconv.ParseFloat(line, 64)
		if err != nil {
			return nil, err
		}
		prices[lineIndex] = floatPrice
	}
	return prices, nil
}