class Solution:
    def isNumber(self, s: str) -> bool:
        seennum = False
        seenexponent = False
        seendecimal = False
        nums = "1234567890"

        for i in range(len(s)):
            if s[i] in nums:
                seennum=True
                
            elif s[i] in "eE":
                if seenexponent or not seennum:
                    return False
                seenexponent=True
                seennum=False
                
            elif s[i]=='.':
                if seendecimal or seenexponent:
                    return False
                seendecimal=True
                
            elif s[i] in "+-":
                if i > 0 and s[i-1] not in "eE":
                    return False
                    
            else:
                return False
                
        return seennum