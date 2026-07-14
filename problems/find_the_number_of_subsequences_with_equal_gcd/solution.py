class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        n=len(nums)
        maxval=max(nums)
        div=10**9+7

        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a

        dp=[[[0]*(maxval+1) for _ in range(maxval+1)] for _ in range(n+1)]
        dp[0][0][0]+=1

        for i in range(1,n+1):
            num=nums[i-1]
            for g1 in range(maxval+1):
                for g2 in range(maxval+1):
                    if dp[i-1][g1][g2]==0:
                        continue
                    ways = dp[i-1][g1][g2]
                    dp[i][g1][g2]=(dp[i][g1][g2]+ways)%div
                    g1next=gcd(g1,num)
                    dp[i][g1next][g2]=(dp[i][g1next][g2]+ways)%div
                    g2next=gcd(g2,num)
                    dp[i][g1][g2next]=(dp[i][g1][g2next]+ways)%div
        ans=0
        for g in range(1,maxval+1):
            ans=(ans+dp[n][g][g])%div
        
        return ans