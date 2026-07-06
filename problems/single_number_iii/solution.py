class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)==2:
            return nums
        xor_all=0
        for num in nums:
            xor_all=xor_all^num
        
        rightmost_bit=xor_all&-xor_all
        unique1=0
        unique2=0

        for num in nums:
            if num & rightmost_bit:
                unique1^=num
            else:
                unique2^=num
        res=[]
        res.append(unique1)
        res.append(unique2)
        return res