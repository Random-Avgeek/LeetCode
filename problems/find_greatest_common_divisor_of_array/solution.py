class Solution:
    def findGCD(self, nums: List[int]) -> int:
        arrmin,arrmax=min(nums),max(nums)
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        return gcd(arrmax,arrmin)