class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If total sum is odd, we cannot split it into two equal integer halves
        if total_sum % 2 != 0: return False
        
        target = total_sum // 2
        n = len(nums)
        
        # dp[i][j] means can we make sum j with first i elements
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        
        # Base case: We can always make a sum of 0 using an empty subset
        for i in range(n + 1):
            dp[i][0] = True
            
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                # Choice 1: Exclude the current number
                dp[i][j] = dp[i-1][j]
                
                # Choice 2: Include the current number (if it doesn't exceed the target)
                if j >= nums[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j - nums[i-1]]
                    
        return dp[n][target]