class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if ")" not in s or "(" not in s:
            return 0
        stack=[-1]
        maxlen=0
        for i in range(0,len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxlen=max(maxlen,i-stack[-1])
        return maxlen