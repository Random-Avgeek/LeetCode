class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        buy = [-prices[0]] * k
        sell = [0] *k

        for price in prices[1:]:
            for j in range(k):
                if j>0:
                    sellprev=sell[j-1]
                else:
                    sellprev=0
                buy[j]=max(buy[j],sellprev-price)
                sell[j]=max(sell[j],buy[j]+price)
        return sell[-1]

