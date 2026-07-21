class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        known={}
        for i in range(len(t)):
            known[t[i]]=known.get(t[i],0)+1
        maxlen=2**31-1
        needed=len(known)
        window_counts={}
        formed=0
        ans=[float('inf'),None,None]
        left=0
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in known and window_counts[char]==known[char]:
                formed+=1
            while left <=right and formed == needed:
                charleft=s[left]
                if right - left + 1< ans[0]:
                    ans = [right-left+1,left,right]
                window_counts[charleft]-=1
                if charleft in known and window_counts[charleft]<known[charleft]:
                    formed-=1
                left+=1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
                