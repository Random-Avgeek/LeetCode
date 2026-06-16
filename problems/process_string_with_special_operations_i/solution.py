class Solution:
    def processStr(self, s: str) -> str:
        res=""
        for char in s:
            if char in "qwertyuiopasdfghjklzxcvbnm":
                res+=char
            if char =="*":
                if len(res)>0:
                    res=res[:-1]
                else:
                    continue
            elif char =="#":
                res+=res
            elif char=="%":
                res=res[::-1]
        return res