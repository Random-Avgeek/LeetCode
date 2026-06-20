class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums)==1:
            return None
        for i in range(0,len(nums)-1):
            minnum=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[minnum]:
                    minnum=j
            nums[minnum],nums[i]=nums[i],nums[minnum]