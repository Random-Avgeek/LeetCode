class Solution:
    def reverseWords(self, s: str) -> str:
        words=list(map(str,s.split()))[::-1]
        finalstr=" ".join(words)
        return finalstr