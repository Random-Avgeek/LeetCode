class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expectedsum=0
        for i in range(1,n+1):
            expectedsum+=i
        actualsum=sum(nums)
        return (expectedsum-actualsum)