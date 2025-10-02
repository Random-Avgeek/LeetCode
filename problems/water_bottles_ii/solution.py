class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        maxBottles=numBottles
        emptyBottles=numBottles
        while emptyBottles>=numExchange:
            emptyBottles-=numExchange
            maxBottles+=1
            numExchange+=1
            emptyBottles+=1
        return maxBottles