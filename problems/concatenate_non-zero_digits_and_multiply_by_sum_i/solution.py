class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:return 0
        totalsum=0
        mynum=""
        while n!=0:
            rem=n%10
            if rem==0:
                n//=10
                continue
            mynum=str(rem)+mynum
            n//=10
            totalsum+=rem
        return (totalsum*int(mynum))