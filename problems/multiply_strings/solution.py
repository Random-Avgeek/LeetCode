class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            onedigit = ord(num1[i]) - ord('0')
            for j in range(len(num2) - 1, -1, -1):
                seconddigit = ord(num2[j]) - ord('0')
                
                product = onedigit * seconddigit
                
                pos1 = i + j
                pos2 = i + j + 1
                
                totalsum = product + res[pos2]
                res[pos2] = totalsum % 10
                res[pos1] += totalsum // 10
        idx = 0
        while idx < len(res) and res[idx] == 0:
            idx += 1
            
        return "".join(map(str, res[idx:]))