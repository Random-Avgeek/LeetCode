class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                
                last_open = stack.pop()
                
                if char == ')' and last_open != '(':
                    return False
                elif char == ']' and last_open != '[':
                    return False
                elif char == '}' and last_open != '{':
                    return False
        
        return not stack