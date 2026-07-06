class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0],-x[1]))
        count=0
        currmax=0
        for _,end in intervals:
            if end>currmax:
                count+=1
                currmax=end
        return count