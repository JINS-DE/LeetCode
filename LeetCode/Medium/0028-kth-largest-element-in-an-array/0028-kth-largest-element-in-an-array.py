"""
정렬 (N log N)이 아닌 heap 자료구조를 사용하여 (N log k) 로 실행
"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        
        return heapq.heappop(heap)
        