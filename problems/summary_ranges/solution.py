class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        summary=[]
        i=0
        while i<len(nums):
            start = nums[i]
            while i+1<len(nums) and nums[i+1]==nums[i]+1:
                i+=1
            if nums[i]==start:
                summary.append(str(start))
            else:
                summary.append(f"{start}->{nums[i]}")
            i+=1
        return summary