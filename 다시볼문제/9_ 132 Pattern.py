from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False  # 132 패턴을 만들 수 있는 요소가 부족할 경우

        # nums[k]를 찾기 위한 변수
        third = float('-inf')
        stack = []

        # 오른쪽에서 왼쪽으로 배열을 탐색
        for i in range(n-1, -1, -1):
            # nums[i]가 nums[k]보다 작다면 132 패턴을 발견
            if nums[i] < third:
                return True
            # stack의 top이 nums[i]보다 작은 동안 pop하여 third 업데이트
            while stack and stack[-1] < nums[i]:
                third = stack.pop()
            # nums[j]로 스택에 저장
            stack.append(nums[i])
        
        return False

    
# 테스트 코드
nums = [1,4,0,-1,-2,-3,-1,-2]
solution = Solution()  # Solution 클래스 인스턴스 생성
result = solution.find132pattern(nums)  # 함수 호출
print(result)  # 결과 출력



# -------Fail---------
# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         stack=[]
#         for i in range(len(nums)):
#             print(f"현재 i: {i}, nums[i]: {nums[i]}, 스택: {stack}")  # 추가된 출력문

#             if not stack:
#                 stack.append(nums[i])
#             if len(stack) == 1:
#                 if stack[-1] > nums[i]:
#                     print(f"1번 패턴에서 pop 후 append: {nums[i]}")  # 추가된 출력문
#                     stack.pop()
#                     stack.append(nums[i])
#                 elif stack[-1] + 1 < nums[i]:
#                     print(f"1번 패턴에서 append: {nums[i]}")  # 추가된 출력문
#                     stack.append(nums[i])

#             elif len(stack) == 2:
#                 if stack[-1] < nums[i]:
#                     print(f"2번 패턴에서 pop 후 append: {nums[i]}") 
#                     stack.pop()
#                     stack.append(nums[i])
#                 elif stack[-1] > nums[i] and stack[0] < nums[i]:
#                     print(f"2번 패턴에서 append: {nums[i]}")  # 추가된 출력문
#                     stack.append(nums[i])
#             if len(stack) == 3:
#                 return True
        
#         return False