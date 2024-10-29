import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # ordertype = 0은 buy 타입, 1은 sell 타입
        buy, sell = [], []

        for price, amount, order_type in orders:
            if order_type:
                heapq.heappush(sell,(price,amount))
            else:
                heapq.heappush(buy,(-price,amount))

            while buy and sell and sell[0][0] <= -buy[0][0]:
                b_p, b_a = heapq.heappop(buy)
                s_p, s_a = heapq.heappop(sell)
            
                if b_a > s_a:
                    heapq.heappush(buy, (b_p, b_a - s_a))  # 남은 buy 수량 다시 추가
                elif b_a < s_a:
                    heapq.heappush(sell, (s_p, s_a - b_a))  # 남은 sell 수량 다시 추가

        answer=0

        while buy or sell:
            if buy:
                b_p, b_a = heapq.heappop(buy)
                answer += b_a
            if sell:
                s_p, s_a = heapq.heappop(sell)
                answer += s_a

        return answer % 1000000007
                    

        