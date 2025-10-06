class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap={}
        for i in range(0,len(nums)):
            complement = target - nums[i]
            if complement in nummap:
                return [nummap[complement],i]
            nummap[nums[i]]=i
                