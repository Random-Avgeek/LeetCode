class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elemsum=0
        digitsum=0
        for i in range(0,len(nums)):
            elemsum+=nums[i]
            while nums[i]>0:
                digitsum+=nums[i]%10
                nums[i]//=10
        return abs(elemsum-digitsum)