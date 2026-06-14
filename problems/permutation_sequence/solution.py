class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(num):
            res = 1
            for i in range(2,num+1):
                res*=i
            return res

        nums = [str(i) for i in range(1,n+1)]
        k=k-1
        res=[]

        for i in range(n-1,-1,-1):
            fact=factorial(i)
            index = k//fact
            res.append(nums.pop(index))
            k=k%fact
        return "".join(res)