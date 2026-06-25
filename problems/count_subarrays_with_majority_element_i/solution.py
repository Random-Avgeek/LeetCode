class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        if target not in nums: return 0
        totalsubarrs=0
        for i in range(0,len(nums)):
            counttarget=0
            for j in range(i,len(nums)):
                if nums[j]==target:
                    counttarget+=1
                if counttarget*2>(j-i+1):
                    totalsubarrs+=1
        return totalsubarrs