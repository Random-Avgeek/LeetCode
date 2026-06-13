class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        finalstr=""
        for word in words:
            wordsum=0
            for char in word:
                wordsum+=weights[ord(char)-ord('a')]
            finalstr+=chr((ord('z')-(wordsum%26)))
        return finalstr
