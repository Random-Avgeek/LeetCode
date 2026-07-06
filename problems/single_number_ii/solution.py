class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones=0
        twos=0
        for num in nums:
            twos |= (num & ones)
            ones=ones^num
            threes=ones&twos

            ones=ones&~threes
            twos=twos&~threes
        return ones