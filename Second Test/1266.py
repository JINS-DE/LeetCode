# class Solution:
#     def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
#         answer=0
#         prev_point = points[0]
#         for i in range(1,len(points)):
#             answer += max( abs(prev_point[0]-points[i][0]),abs(prev_point[1]-points[i][1]) )    
#             prev_point = points[i]
#         return answer


dic = {4:1}
dic[1]-=1
print(dic)