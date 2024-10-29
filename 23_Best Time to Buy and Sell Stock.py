# 카데인 알고리즘 (max, min)활용 코드
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_cell = 0
        min_price = float("inf")
        for price in prices:
            min_price=min(price,min_price)
            max_cell=max(max_cell,price-min_price)
        return max_cell

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = float('inf')  # 초기 최소 가격을 무한대 설정
#         max_profit = 0  # 초기 최대 이익은 0으로 설정

#         # prices 배열 순회
#         for price in prices:
#             # 현재 가격과 최소 구매 가격을 비교하여 갱신
#             min_price = min(min_price, price)
#             # 현재 가격에서 최소 구매 가격을 뺀 값과 기존 최대 이익을 비교하여 갱신
#             max_profit = max(max_profit, price - min_price)
        
#         return max_profit


# # 완탐
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_sell = 0
#         for i in range(len(prices)-1):
#             for j in range(i+1,len(prices)):
#                 max_sell=max(-(prices[i]-prices[j]),max_sell)
                
#         return max_sell