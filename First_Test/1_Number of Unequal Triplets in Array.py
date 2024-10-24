from typing import List
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        answer = 0 
        size=len(nums)
        for i in range(size):
            for j in range(1,size):
                for k in range(2,size):
                    if nums[i]<nums[j]<nums[k]:
                        answer+=1
        return answer
        
# 테스트 코드
nums = [4,4,2,4,3]
solution = Solution()  # Solution 클래스 인스턴스 생성
result = solution.unequalTriplets(nums)  # 함수 호출
print(result)  # 결과 출력