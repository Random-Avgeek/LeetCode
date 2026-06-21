class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows=1
        arrowpos=points[0][1]

        for i in range(1,len(points)):
            if points[i][0]>arrowpos:
                arrows+=1
                arrowpos=points[i][1]
        
        return arrows