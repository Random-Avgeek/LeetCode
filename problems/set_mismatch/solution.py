class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        totalsum=n*(n+1)//2
        uniquesum=sum(set(nums))
        actualsum=sum(nums)
        duplicate=actualsum-uniquesum
        missing=totalsum-uniquesum
        return[duplicate,missing]