class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        revnum = 0
        while temp != 0:
            revnum = revnum * 10 + temp % 10
            temp //= 10
        if revnum >= 2**31:
            return False
        elif revnum != x:
            return False
        else:
            return True
