INT_MAX=2**31-1
INT_MIN=-2**31

class Solution:
    def helper(self,s:str,i:int,num:int,sign):
        if i>=len(s) or not s[i].isdigit():
            return sign*num
        num=num*10+int(s[i])
        if sign*num<=INT_MIN: return INT_MIN
        elif sign*num>=INT_MAX: return INT_MAX
        return self.helper(s,i+1,num,sign)
    def myAtoi(self, s: str) -> int:
        i=0
        while i < len(s) and s[i]==' ':
            i+=1
        sign=1
        if i<len(s) and (s[i]=='-' or s[i]=='+'):
            sign=-1 if s[i]=='-' else 1
            i+=1
        return self.helper(s,i,0,sign)

        