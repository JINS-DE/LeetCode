"""
# 투포인터 풀이
완전 탐색 풀이에서 착안, 
어찌됐든 현재 물 높이는 왼쪽에서 가장 높은 물 높이, 오른쪽에서 가장 높은 물높이 중에
고인 물의 양은 가장 낮은 물높이 - 현재 물높이이다.

height[left] < height[right] 이면 왼쪽의 높이만 생각하면된다. 
height[left] >= height[right] 이면 오른쪽의 높이만 생각하면 된다. 

변수 정의
left, right = 0, n-1
left_max, right_max = 0,0
answer = 0

------
# STACK 풀이
stack에는 index가 저장

1. 트리거 작동: 물 높이가 높아질 때 
- height[stack[-1]] < now_height 
- bottom = stack.pop() # 현재 바닥 높이

2. 왼쪽 벽 찾기 : 
left_wall = stack[-1] 

물 웅덩이의 높이 : h = min(now_height,height[left_wall])-height[bottom]
웅덩이의 가로 길이 : w = i-left_wall-1

# 브루스 포스 (시간초과)
for i in range(n):
    left_max = max(height[:i+1])
    right_max = max(height[i:])
    total+=min(left_max,right_max)-height[i]
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left, right = 0, n-1
        left_max, right_max = 0,0
        answer = 0
        while left<right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    answer+=left_max-height[left]
                left+=1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    answer+=right_max-height[right]
                right-=1
        return answer