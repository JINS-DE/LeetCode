"""
prefix sum 문제
- 인덱스 i ~ j까지의 합 = (0부터 j까지의 합) - (0부터 i-1까지의 합)
- sum(i, j) = prefix_sum[j] - prefix_sum[i-1] 인데 우리는 sum(i,j)가 k인 값을 찾고 있다. 
    k = prefix_sum[j] - prefix_sum[i-1]
    -> prefix_sum[i-1] = prefix_sum[j] - k
    -> 이전까지의 prefix_sum을 hash로 저장하여 hash[prefix_sum[j] - k] 값을 찾으면 된다. 
    -> 찾으면 answer += hash[prefix_sum[j] - k]
- 같은 prefix_sum이 여러번 나왔을 수 있으니 딕셔너리로 +1씩해준다.
"""

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer=0
        prefix_sum=0

        dic = defaultdict(int)
        dic[0]+=1

        for num in nums:
            # 1. 현재까지의 누적 합 계산
            prefix_sum += num

            # 2. 과거 누적합 중 diff이 있었는지 확인
            diff = prefix_sum-k
            if diff in dic:
                answer+=dic[diff]
            dic[prefix_sum]+=1

        return answer

