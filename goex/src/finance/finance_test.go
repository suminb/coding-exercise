package finance

import "testing"

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

func TestRebalance(t *testing.T) {

}
