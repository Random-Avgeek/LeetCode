class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqlist = []
        for i in range(0, 100):
            freqlist.append(0)
        for i in range(0, len(nums)):
            freqlist[nums[i] - 1] += 1
        f = max(freqlist)
        c = 0
        for i in range(0, 100):
            if freqlist[i] == f:
                c += freqlist[i]
        return c
