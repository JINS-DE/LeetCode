class Solution(object):
    def merge(self, intervals):
        intervals.sort()

        answer = []
        prev = intervals[0]

        for i in range(1,len(intervals)):
            curr = intervals[i]

            if prev[1] >= curr[0]:
                prev[1] = max(prev[1],curr[1])
            else:
                answer.append(prev)
                prev = curr
        
        answer.append(prev)

        return answer


        