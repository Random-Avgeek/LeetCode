class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(low,high):
            if low > high:
                return -1
            mid = (low + high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return binary(mid+1,high)
            else:
                return binary(low,mid-1)
        return binary(0,len(nums)-1)