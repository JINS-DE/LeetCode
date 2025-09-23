class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_price=float("inf")
        for price in prices:
            profit = max(profit,price-min_price)
            min_price = min(price,min_price)
        return profit