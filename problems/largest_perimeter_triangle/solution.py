class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums=sorted(nums)
        nums=nums[::-1]
        print(nums)
        for i in range(0,len(nums)-2):
            if nums[i]<nums[i+1]+nums[i+2]:
                maxperim=nums[i]+nums[i+1]+nums[i+2]
                return maxperim
            else:
                continue
        return 0