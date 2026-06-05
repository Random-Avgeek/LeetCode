class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        speccount=0
        seen=[]
        for char in word:
            if char not in seen and chr(ord(char)-32) in word:
                seen.append(char)
                speccount+=1
        return speccount