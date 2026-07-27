class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s==0:
            return 0
        if s>9*n:
            return -1
        maxnum=0
        while n>0:
            for i in range(9,-1,-1):
                if (s-i)>-1:
                    s-=i
                    maxnum+=i*10**(n-1)
                    break
            n-=1
        return maxnum