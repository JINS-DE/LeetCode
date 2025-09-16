/*
정렬 후 고정된 nums[i] 기준으로 투 포인터 방식으로 3sum 구하기
3sum = nums[i] + nums[j] + nums[k]
- 3sum == 0 인 경우 j++ , k--
- 3sum > 0 인 경우 k--
- 3sum < 0 인 경우 j++

중복된 값 건너뛰기
- 이전 값이 같을 때
- i,j 는 ++, k는 --
*/

import java.util.*;
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        Arrays.sort(nums);
        for (int i=0; i<nums.length-2; i++){
            if (i>0 && nums[i]==nums[i-1]) {
                continue;}

            int j = i+1;
            int k = nums.length-1;
            
            while (j<k) {
                int total = nums[i] + nums[j] + nums[k];
                if (total < 0 ){
                    j++;
                } else if (total > 0){
                    k--;
                } else {
                    answer.add(Arrays.asList(nums[i],nums[j],nums[k]));
                    j++;
                    k--;
                    while (j < k && nums[j] == nums[j-1]) j++;
                    while (j < k && nums[k] == nums[k+1]) k--;
                    
                }
            }
        }
        // System.out.println(nums[0]);
        return answer;
    }
}