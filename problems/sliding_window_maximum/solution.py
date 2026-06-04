from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        if k == 1:
            return nums
        left_max = [0] * n
        right_max = [0] * n
        for i in range(n):
            if i % k == 0:
                left_max[i] = nums[i]
            else:
                left_max[i] = max(left_max[i - 1], nums[i])
        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:
                right_max[i] = nums[i]
            else:
                right_max[i] = max(right_max[i + 1], nums[i])
        result = []
        for i in range(n - k + 1):
            j = i + k - 1
            window_max = max(right_max[i], left_max[j])
            result.append(window_max)
            
        return result