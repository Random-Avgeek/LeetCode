class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products=[]
        totalproduct=1
        numzeroes=0
        for num in nums:
            if num!=0:
                totalproduct*=num
            if num==0:
                numzeroes+=1
        if numzeroes>1:
            return [0]*len(nums)
        for num in nums:
            if num==0:
                products.append(totalproduct)
            else:
                if numzeroes==1:
                    products.append(0)
                else:
                    products.append(totalproduct//num)
        return products