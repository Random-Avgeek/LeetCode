class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost)<3:
            return sum(cost)
        cost = sorted(cost,reverse=True)
        mincost=0
        for i in range(0,len(cost)):
            if (i+1)%3!=0:
                mincost+=cost[i]
        return mincost