class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0

        for sell in range(len(prices)):
            if prices[buy] > prices[sell]:
                buy = sell
                
            profit = max(profit, prices[sell] - prices[buy])

        return profit