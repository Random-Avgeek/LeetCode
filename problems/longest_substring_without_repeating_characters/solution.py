class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        maxlen=1
        left=0
        seen=set()
        for right in range(len(s)):
            if s[right] in seen:
                while s[left]!=s[right]:
                    seen.remove(s[left])
                    left+=1
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            maxlen=max(maxlen,right-left+1)
        return maxlen

        