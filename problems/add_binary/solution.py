class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=[]
        carry=0
        i=len(a)-1
        j=len(b)-1

        while i>=0 or j>=0 or carry:
            val1=int(a[i]) if i>= 0 else 0
            val2=int(b[j]) if j>= 0 else 0

            total = val1+val2+carry
            char = str(total % 2)
            carry = total // 2
        
            res.append(char)
            i -= 1
            j -= 1
            
        return "".join(reversed(res))
