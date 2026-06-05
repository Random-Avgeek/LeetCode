class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<1:
            return [-1,-1]
        elif len(nums)==1:
            if target in nums:
                return [0,0]
            else:
                return [-1,-1]
        numfound=[-1,-1]
        for i in range(0,len(nums)):
            j=len(nums)-i-1
            if -1 not in numfound:
                break
            if numfound[0]==-1 and nums[i]==target:
                numfound[0]=i
            if numfound[1]==-1 and nums[j]==target:
                numfound[1]=j
        return numfound