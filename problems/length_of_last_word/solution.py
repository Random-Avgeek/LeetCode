class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordlist=s.split()
        return len(wordlist[-1])