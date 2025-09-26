class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        if n < 3:
            return 0
        for i in range(n - 1, 1, -1):
            c = nums[i]
            l, r = 0, i - 1
            
            while l < r:
                a = nums[l]
                b = nums[r]
                if a + b > c:
                    count += (r - l)
                    r -= 1
                else:
                    l += 1
        return count