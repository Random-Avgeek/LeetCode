class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        for i in range(0,n):
            tempnums=[]
            for j in range(0,len(nums)-1):
                x=(nums[j]+nums[j+1])%10
                tempnums.append(x)
            if len(tempnums)==1:
                return tempnums[0]
            else:
                nums=tempnums