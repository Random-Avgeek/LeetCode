class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for x in range(2, n):
            for i in range(n - x):
                j = i + x
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    triangle_score = values[i] * values[k] * values[j]
                    current_score = triangle_score + dp[i][k] + dp[k][j]
                    dp[i][j] = min(dp[i][j], current_score)
        return dp[0][n - 1]