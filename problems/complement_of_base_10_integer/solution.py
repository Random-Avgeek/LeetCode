class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        temp=n
        bits=0
        while temp>0:
            temp//=2
            bits+=1
        total=(2**bits)-1
        return total - n