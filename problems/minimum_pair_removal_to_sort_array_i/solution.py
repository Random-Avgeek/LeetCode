class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        ops = 0
        
        # Helper function to check if the array is already sorted (non-decreasing)
        def is_sorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        # Keep merging the smallest adjacent pair until the array is sorted
        while not is_sorted(nums):
            min_sum = float('inf')
            min_idx = -1
            
            # Find the pair with the minimum sum (leftmost tie-breaker is implicit via '<')
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    min_idx = i
            
            # Replace the pair at min_idx with their sum
            nums[min_idx] = min_sum
            nums.pop(min_idx + 1)
            
            ops += 1
            
        return ops