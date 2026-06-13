class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp=[[] for _ in range(n+1)]
        dp[0]=[""]

        for i in range(1,n+1):
            for j in range(i):
                left=dp[j]
                right=dp[i-j-1]
                for l in left:
                    for r in right:
                        dp[i].append("("+l+")"+r)
        return dp[n]


