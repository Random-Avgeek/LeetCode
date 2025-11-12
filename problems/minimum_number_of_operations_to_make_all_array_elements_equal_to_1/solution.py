class Solution:
    def minOperations(self, nums: List[int]) -> int:
            from math import gcd
            n = len(nums)
            if 1 in nums:
                return sum(1 for x in nums if x != 1)
            minlength = float('inf')
            for i in range(n):
                curr = nums[i]
                for j in range(i+1, n):
                    curr = gcd(curr, nums[j])
                    if curr == 1:
                        minlength = min(minlength, j - i + 1)
                        break
            if minlength == float('inf'):
                return -1
            return minlength - 1 + n - 1