class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0]*n
        if obstacleGrid[0][0]==1:
            return 0
        else:
            dp[0]=1
            for i in range(0,m):
                for j in range(0,n):
                    if i==0 and j==0:
                        continue
                    if obstacleGrid[i][j]==1:
                        dp[j]=0
                    elif j>0:
                        dp[j]+=dp[j-1]
        return dp[n-1]