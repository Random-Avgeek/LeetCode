class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        totalzeroes=0
        pow=1
        while n>=5**pow:
            pow+=1
        pow-=1
        for i in range(1,pow+1):
            totalzeroes+=n//5**i
        return totalzeroes