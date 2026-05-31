class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        
        while i < n and s[i] == ' ':
            i += 1
            
        isNegative = False
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                isNegative = True
            i += 1
        final_num = 0
        while i < n and s[i].isdigit():
            final_num = final_num * 10 + int(s[i])
            i += 1
        if isNegative:
            final_num = -final_num
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if final_num < INT_MIN:
            return INT_MIN
        if final_num > INT_MAX:
            return INT_MAX
            
        return final_num