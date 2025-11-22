class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        threecount = 0
        for i in range (0,len(nums)):
            if nums[i]%3==0:
                continue
            elif nums[i]%3!=0:
                threecount+=1
        return threecount