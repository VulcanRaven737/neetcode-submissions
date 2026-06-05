class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for j in prices:
            buy = min(buy, j)
            profit = max(profit, j-buy)

        return profit