class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counteven=0
        if len(nums)==0:
            return 0
        for n in nums:
            numlen=0
            while n>0:
                numlen+=1
                n=n//10
            if numlen%2==0:
                counteven+=1
        return counteven
