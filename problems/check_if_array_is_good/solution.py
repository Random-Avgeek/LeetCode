class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maxnum=max(nums)
        if len(nums)!=maxnum+1:
            return False
        else:
            nums=sorted(nums)
            unique=set(nums)
            if len(unique)==maxnum and nums[-1] == maxnum and nums[-2] == maxnum:
                return True
            else:
                return False