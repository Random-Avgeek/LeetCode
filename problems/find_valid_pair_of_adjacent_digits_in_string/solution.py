class Solution:
    def findValidPair(self, s: str) -> str:
        freqmap={}
        for i in range(0,len(s)):
            if s[i] in freqmap:
                freqmap[s[i]]+=1
            else:
                freqmap[s[i]]=1
        finalstr=""
        for i in range(0,len(s)-1):
            if s[i]!=s[i+1] and freqmap[s[i]]==int(s[i]) and freqmap[s[i+1]]==int(s[i+1]):
                finalstr+=f"{s[i]}{s[i+1]}"
                break
        return finalstr