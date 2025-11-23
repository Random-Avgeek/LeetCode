class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        remainder = total_sum % 3

        if remainder == 0:
            return total_sum

        mod1 = []
        mod2 = []

        for num in nums:
            if num % 3 == 1:
                mod1.append(num)
            elif num % 3 == 2:
                mod2.append(num)

        mod1.sort()
        mod2.sort()

        option1 = float('-inf')
        option2 = float('-inf')

        if remainder == 1:
            if mod1:
                option1 = total_sum - mod1[0]
            if len(mod2) >= 2:
                option2 = total_sum - mod2[0] - mod2[1]
        else:
            if mod2:
                option1 = total_sum - mod2[0]
            if len(mod1) >= 2:
                option2 = total_sum - mod1[0] - mod1[1]

        return max(option1, option2)