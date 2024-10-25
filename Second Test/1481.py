
from typing import List
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        dic_li = sorted(dic.items(), key=lambda x:x[1])

        for i,val in dic_li:
            if k==0:
                break
            k -= dic[i]
            if k>=0:
                del dic[i]
                    
        return len(dic)

# 테스트 코드
nums = [4,4,2,4,3]
k=2
solution = Solution()  # Solution 클래스 인스턴스 생성
result = solution.findLeastNumOfUniqueInts(nums,k)  # 함수 호출
print(result)  # 결과 출력

