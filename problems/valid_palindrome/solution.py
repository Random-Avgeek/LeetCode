class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9 ]', '', s)
        s = s.replace(" ","").lower()
        return s == s[::-1]