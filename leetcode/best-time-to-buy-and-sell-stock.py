# 121. Best Time to Buy and Sell Stock
# difficulty: easy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

import pytest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            if p - min_price > max_profit:
                max_profit = p - min_price

        return max_profit


@pytest.mark.parametrize('values, expected', [
    ([], 0),
    ([1], 0),
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([2, 1, 4], 3),
    ([2, 4, 1], 2),
])
def test(values, expected):
    s = Solution()
    assert expected == s.maxProfit(values)


if __name__ == '__main__':
    pytest.main(['-v', 'best-time-to-buy-and-sell-stock.py'])