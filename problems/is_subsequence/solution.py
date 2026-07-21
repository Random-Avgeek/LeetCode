class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t)<len(s):
            return False
        if s=="":
            return True
        ptr1=0
        for i in range(len(t)):
            if ptr1>len(s)-1:
                break
            if t[i]==s[ptr1]:
                ptr1+=1
        if ptr1<len(s):
            return False
        return True