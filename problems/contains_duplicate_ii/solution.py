class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nummap={}
        for i in range(0,len(nums)):
            if nums[i] in nummap:
                if abs(i-nummap[nums[i]])<=k:
                    return True
            nummap[nums[i]]=i
        return False