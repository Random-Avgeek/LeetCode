#optimizing now to try better solution
#dp[j]=dp[j]+dp[j-1]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n==1 or m==1:
            return 1
        dp=[1]*n
        for i in range(1,m):
            for j in range(1,n):
                dp[j]=dp[j]+dp[j-1]
        return dp[n-1]