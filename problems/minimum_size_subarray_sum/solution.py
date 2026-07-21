class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        left=0
        total=0
        size=float('inf')
        for i in range(0,len(nums)): #i acts as the right pointer here
            total+=nums[i]
            if total>=target:
                while total>=target:
                    size=min(size,i-left+1)
                    total-=nums[left]
                    left+=1
        return size if size<=len(nums) else 0