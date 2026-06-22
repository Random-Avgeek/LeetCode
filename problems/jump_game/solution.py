class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if 0 not in nums:
            return True
        maxreach=0
        for i in range(len(nums)):
            if i > maxreach:
                return False
            maxreach = max(maxreach,i+nums[i])
            if maxreach>len(nums)+1:
                return True
        return True
        
