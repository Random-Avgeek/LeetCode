class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Frequency Map / Array for each character
        anag={}
        for s in strs:
            count=[0]*26
            for char in s:
                count[ord(char)-ord('a')]+=1
            key = tuple(count)
            if key not in anag:
                anag[key]=[]
            
            anag[key].append(s)
        return list(anag.values())