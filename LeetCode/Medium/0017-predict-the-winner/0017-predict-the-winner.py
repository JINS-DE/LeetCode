class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # 1. '노트' 생성: 결과를 저장할 2D 리스트
        # 아직 계산되지 않았다는 것을 표시하기 위해 None으로 초기화합니다.
        memo = [[None] * n for _ in range(n)]

        def solve(i, j):
            # 2. '노트' 확인: 계산 전에 캐시부터 확인
            if memo[i][j] is not None:
                return memo[i][j]

            # 기저 사례: 남은 숫자가 하나일 때
            if i == j:
                return nums[i] # 이 경우는 바로 반환하므로 굳이 저장할 필요는 없음

            # 재귀 계산 로직 (기존과 동일)
            pick_left = nums[i] - solve(i + 1, j)
            pick_right = nums[j] - solve(i, j - 1)
            
            result = max(pick_left, pick_right)

            # 3. '노트'에 기록: 반환하기 전에 계산 결과를 저장
            memo[i][j] = result
            
            return result

        # 최종 결과 계산
        return solve(0, n - 1) >= 0