class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_v = 0  # 지금까지 본 최대값
        max_diff = 0  # 최대 차이 (max_v - nums[j])
        max_triplet = 0  # 최종 최대 트리플릿 값
        
        for curr in nums:
            # 현재 요소에 대한 최대 트리플릿 값 계산
            max_triplet = max(max_triplet, max_diff * curr)
            # 현재 값과의 차이의 최대값 업데이트
            max_diff = max(max_diff, max_v - curr)
            # 지금까지 본 최대값 업데이트
            max_v = max(max_v, curr)

        return max_triplet  # 최종 최대값 반환