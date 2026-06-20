class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen={}
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]]=[1,i]
            else:
                seen[s[i]][0]+=1
        print(seen)
        for count,index in seen.values():
            if count==1:
                return index
        return -1