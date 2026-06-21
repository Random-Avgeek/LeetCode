class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if coins<min(costs):
            return 0
        elif coins>sum(costs):
            return len(costs)
        costs=sorted(costs)
        i=0
        count=0
        while coins>=0:
            if coins-costs[i]<0:
                break
            coins-=costs[i]
            i+=1
            count+=1
        return count