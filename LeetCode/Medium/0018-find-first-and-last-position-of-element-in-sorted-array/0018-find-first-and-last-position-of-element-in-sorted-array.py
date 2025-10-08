class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n==0: return [-1,-1]

        left,right = 0, n-1
        flag = False
        while left<=right:
            mid = (left+right)//2
            if target<nums[mid]:
                right=mid-1
            elif target > nums[mid]:
                left=mid+1
            else:
                flag=True
                break
        
        if flag:
            ltmp=rtmp=mid
            while 0<=ltmp and nums[ltmp]==target:
                left = ltmp
                ltmp-=1
            
            while rtmp<n and nums[rtmp]==target:
                right = rtmp
                rtmp+=1
            return [left,right]        

        else:
            return [-1,-1]

        
        