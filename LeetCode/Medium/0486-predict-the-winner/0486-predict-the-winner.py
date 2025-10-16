# 복습용 
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        
        # 항상 최적의 선택을 도출하는 함수
        def best_choice(i,j):
            if i==j:
                return nums[i]
            
            left_choice = nums[i] - best_choice(i+1,j)
            right_choice = nums[j] - best_choice(i,j-1)

            return max(left_choice,right_choice)
            
        return best_choice(0,n-1) >= 0