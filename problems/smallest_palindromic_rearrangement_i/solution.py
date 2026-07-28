class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26
        for char in s:
            freq[ord(char)-ord('a')]+=1
        odd_count=0
        odd_char=""

        for i in range(26):
            if freq[i]%2!=0:
                odd_count+=1
                odd_char=chr(i+ord('a'))
        
        left = "".join(chr(i + ord('a'))*(freq[i] // 2) for i in range(26))
        return left + odd_char+left[::-1]
