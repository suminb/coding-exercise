package finance

import (
	"math"
	"testing"
)

const delta = 0.000001

var portfolio Portfolio

func init() {
	records := []PortfolioRecord{
		{Asset: Asset{Name: "NVDA", Type: Stock, UnitPrice: 190}, Quantity: 200},
		{Asset: Asset{Name: "AMD", Type: Stock, UnitPrice: 28}, Quantity: 1480},
		{Asset: Asset{Name: "AMZN", Type: Stock, UnitPrice: 1850}, Quantity: 100},
	}

	portfolio = Portfolio{Records: records}
}

func TestPortfolio_CalcNetAssetValue(t *testing.T) {
	nav := portfolio.CalcNetAssetValue()
	if nav != (190*200 + 28*1480 + 1850*100) {
		t.Errorf("Wrong NAV: %f\n", nav)
	}
}

func TestPortfolioRecord_CurrentShare(t *testing.T) {
	shares := []float64{0.1436998941, 0.1567085161, 0.6995915898}

	for i, record := range portfolio.Records {
		currentShare := record.CurrentShare(&portfolio)
		if math.Abs(currentShare-shares[i]) > delta {
			t.Errorf("Incorrect share (%f) for asset %s\n", currentShare, record.Asset.Name)
		}
	}
}

func TestRebalance(t *testing.T) {

}
