class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        appearance={}
        for char in magazine:
            if char in appearance:
                appearance[char]+=1
            else:
                appearance[char]=1
        
        for char in ransomNote:
            if char not in appearance:
                return False
            elif char in appearance and appearance[char]>0:
                appearance[char]-=1
            else:
                return False
        return True