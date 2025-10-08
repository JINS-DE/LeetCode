class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = intervals[0]
        answer=[]
        for interval in intervals[1:]:
            if prev[1] >= interval[0]:
                prev[1] = max(prev[1],interval[1])
            else:
                answer.append(prev)
                prev=interval
        answer.append(prev)
        return answer