class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=0
        minprice=prices[0]
        for i in range(1,len(prices)):
            minprice=min(minprice,prices[i])
            maxprof=max(maxprof,(prices[i]-minprice))
        return maxprof