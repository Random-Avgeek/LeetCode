class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        maxlen=1
        n=len(s)
        for i in range(0,n-1):
            seen=[]
            seen.append(s[i])
            length=1
            for j in range (i+1,n):
                if s[j] not in seen:
                    seen.append(s[j])
                    length+=1
                    maxlen=max(length,maxlen)
                else:
                    break
        return maxlen