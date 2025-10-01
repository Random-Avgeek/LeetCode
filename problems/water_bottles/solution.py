class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totaldrink=numBottles
        emptybottles=numBottles
        while emptybottles>=numExchange:
            newbottles=emptybottles//numExchange
            totaldrink+=newbottles
            emptybottles=newbottles+emptybottles%numExchange
        return totaldrink