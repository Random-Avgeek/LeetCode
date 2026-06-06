class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        sumdiffs=[]
        if len(nums)==1:
            return [0]
        leftsum=0
        rightsum=sum(nums)-nums[0]
        sumdiffs.append(rightsum-leftsum)
        for i in range(1,len(nums)):
            leftsum += nums[i-1]
            rightsum-=nums[i]
            sumdiffs.append(abs(leftsum-rightsum))
        return sumdiffs