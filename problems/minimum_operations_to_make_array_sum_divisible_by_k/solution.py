class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arrsum=sum(nums)
        mod=arrsum%k
        negops=mod
        return negops