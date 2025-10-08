class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_price = float("-inf")
        for price in prices:
            min_price=min(min_price,price)
            max_price = max(max_price, price-min_price)
        return max_price