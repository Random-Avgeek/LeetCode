class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1,0])
        restrictions.append([n, n - 1])
        restrictions.sort()
        for i in range(1,len(restrictions)):
            dist = restrictions[i][0]-restrictions[i-1][0]
            restrictions[i][1]=min(restrictions[i][1],restrictions[i-1][1]+dist)

        for i in range(len(restrictions)-2,-1,-1):
            dist=restrictions[i+1][0]-restrictions[i][0]
            restrictions[i][1]=min(restrictions[i][1], restrictions[i+1][1] + dist)

        maxh=0
        for i in range(len(restrictions)-1):
            h1,h2=restrictions[i][1],restrictions[i+1][1]
            idx1, idx2 = restrictions[i][0], restrictions[i+1][0]
            dist = idx2-idx1
            peak = (h1+h2+dist)//2
            maxh=max(maxh,peak)
        return maxh