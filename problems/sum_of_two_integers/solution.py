class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b!=0:
            startsum=(a^b)&mask
            carry = ((a&b)<<1)&mask
            a= startsum
            b= carry
        if a<0x7FFFFFFF:
            return a
        else:
            return ~(a^mask)