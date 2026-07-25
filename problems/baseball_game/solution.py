class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for char in operations:
            if char == "C":
                stack.pop()
            elif char == "D":
                num=stack[-1]
                stack.append(num*2)
            elif char == "+":
                num1=stack[-1]
                num2=stack[-2]
                stack.append(num1+num2)
            else:
                stack.append(int(char))
        return sum(stack)