// 121. Best Time to Buy and Sell Stock
// difficulty: easy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

package leetcode

import (
	"fmt"
	"testing"
)

func maxProfit(prices []int) int {
	n := len(prices)
	if n < 2 {
		return 0
	}

	minPrice := prices[0]
	maxProfit := 0

	for _, price := range prices {
		if price < minPrice {
			minPrice = price
		}
		profit := price - minPrice
		if profit > maxProfit {
			maxProfit = profit
		}
	}

	return maxProfit
}

func TestMaxProfit(t *testing.T) {
	params := []struct {
		value    []int
		expected int
	}{
		{[]int{}, 0},
		{[]int{1}, 0},
		{[]int{7, 1, 5, 3, 6, 4}, 5},
		{[]int{7, 6, 4, 3, 1}, 0},
		{[]int{2, 1, 4}, 3},
		{[]int{2, 4, 1}, 2},
	}

	for _, param := range params {
		assertEquals(t, param.expected, maxProfit(param.value),
			fmt.Sprintf("Case %#v", param.value))
	}
}
