class Solution:
    def maxProduct(self, n: int) -> int:
        top1=0
        top2=0
        while n>0:
            rem=n%10
            if rem>top1:
                top2=top1
                top1=rem
            elif rem>top2:
                top2=rem
            n//=10
        return top1*top2