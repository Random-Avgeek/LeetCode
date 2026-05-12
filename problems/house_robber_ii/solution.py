class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        elif n==2:
            return max(nums[0],nums[1])
        
        def robcircle(arr):
            dp=[0]*len(arr)
            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])
            for i in range(2,len(arr)):
                dp[i]=max(dp[i-1],arr[i]+dp[i-2])
            return dp[len(arr)-1]
            
        return max(robcircle(nums[0:-1]),robcircle(nums[1:]))