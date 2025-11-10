class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        stack = [0] * (n + 1)
        ops=0
        top=0
        for num in nums:
            while stack[top]>num:
                top-=1
                ops+=1
            if stack[top]!=num:
                top+=1
                stack[top]=num
        return ops + top