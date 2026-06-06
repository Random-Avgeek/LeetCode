class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold=-prices[0]
        free=0
        for price in prices[1:]:
            prev_hold=hold
            prev_free=free
            hold = max(prev_hold, prev_free-price)
            free = max(prev_free, prev_hold+price)

        return free
