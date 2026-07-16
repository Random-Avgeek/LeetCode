class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        explen=len(words)*len(words[0])
        word_len=len(words[0])
        instance={}
        for word in words:
            if word in instance:
                instance[word]+=1
            else:
                instance[word]=1
        if len(s)<explen:
            return []
        res=[]
        for i in range(len(s)-explen+1):
            substr=s[i:i+explen]
            seen={}
            present=True
            for j in range(0,explen,word_len):
                chunk = substr[j:j+word_len]
                if chunk not in instance:
                    present=False
                    break
                seen[chunk]=seen.get(chunk,0)+1
                if seen[chunk]>instance[chunk]:
                    present=False
                    break
            if present==True:
                res.append(i)
        return res