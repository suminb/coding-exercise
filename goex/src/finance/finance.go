package finance

type Portfolio struct {
	Records []PortfolioRecord
}

type PortfolioRecord struct {
	Asset    Asset
	Quantity float64
}

type Asset struct {
	Name      string
	Type      AssetType
	UnitPrice float64
}

type AssetType int

const (
	Unknown AssetType = 0
	Cash    AssetType = 1
	Bond    AssetType = 2
	Stock   AssetType = 3
)

func (portfolio *Portfolio) CalcNetAssetValue() float64 {
	netAssetValue := 0.0
	for _, record := range portfolio.Records {
		netAssetValue += record.Asset.UnitPrice * record.Quantity
	}
	return netAssetValue
}

func Rebalance() {

}
