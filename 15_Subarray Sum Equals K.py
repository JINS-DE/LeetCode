from typing import List
from collections import defaultdict
''' 누적합 계산법 
부분 배열 합=누적합[j]−누적합[i-1]
누적합[i-1] = 누적합[j] - k
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0: 1}  # 초기화: 부분합이 0인 경우를 1로 설정
        runningSum = 0  # 현재까지의 부분합
        count = 0  # 합이 k인 부분 배열의 개수

        for num in nums:
            runningSum += num  # 현재 숫자를 추가하여 부분합 갱신
            
            difference = runningSum - k  # 현재 부분합에서 k를 뺀 값
            
            if difference in dic:
                count += dic[difference]  # difference에 해당하는 횟수만큼 count 증가
            
            if runningSum in dic:
                dic[runningSum] += 1  # 현재 부분합의 출현 횟수를 1 증가
            else:
                dic[runningSum] = 1  # 처음 등장하는 부분합을 1로 초기화

        return count  # 최종 카운트 반환

''' 완전탐색 '''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        
        # 모든 부분 배열을 탐색
        for left in range(len(nums)):
            sums = 0
            for right in range(left, len(nums)):
                sums += nums[right]  # right 포인터를 이동하며 합을 누적
                if sums == k:
                    answer += 1

        return answer
