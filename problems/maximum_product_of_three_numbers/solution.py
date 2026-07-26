class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        nums.sort()
        prod1=nums[-1]*nums[-2]*nums[-3]
        prod2=nums[0]*nums[1]*nums[-1]
        if prod1>prod2:
            return prod1
        else: return prod2