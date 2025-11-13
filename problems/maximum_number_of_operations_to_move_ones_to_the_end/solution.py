class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        ops = 0
        for i, c in enumerate(s):
            if c == '1':
                ones += 1
            elif i > 0 and s[i - 1] == '1':
                ops += ones
        return ops