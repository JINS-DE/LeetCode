
"""
# 현재 물의 높이 계산 법 : 
min_top = 나의 왼쪽에서 가장 높은 것탑과 나의 오른쪽에서 가장 높은 탑 중 낮은 탑을 고른다.
현재 나의 물높이 = min_top - 나의 높이
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0

        # 브루스 포스 (시간초과)
        # for i in range(n):
        #     left_max = max(height[:i+1])
        #     right_max = max(height[i:])
        #     total+=min(left_max,right_max)-height[i]

        # 스택
        stack = []
        total = 0

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom = stack.pop()

                if not stack: # 왼쪽 벽이 없는 경우
                    break
                left = stack[-1]

                water_width = i-left-1
                water_height = min(h,height[left])- height[bottom]
                total += water_width*water_height
            stack.append(i)
            
        return total
