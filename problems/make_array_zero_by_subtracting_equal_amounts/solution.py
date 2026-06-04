class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen=[]
        count=0
        for i in range(0,len(nums)):
            if nums[i]!=0 and nums[i] not in seen:
                seen.append(nums[i])
                count+=1
        return count