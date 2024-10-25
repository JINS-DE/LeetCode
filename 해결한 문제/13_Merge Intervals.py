class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer=[]
        intervals.sort()
        merge_li = intervals[0]
        for i in range(1,len(intervals)):
            if merge_li[1] >= intervals[i][0]:
                merge_li[1] = max(merge_li[1], intervals[i][1])
            else:
                answer.append(merge_li)
                merge_li = intervals[i]
        answer.append(merge_li)
        return answer
