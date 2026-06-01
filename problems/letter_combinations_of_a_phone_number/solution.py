class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digitsmap = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }        
        res = [""]
        for digit in digits:
            combinations = []
            for combination in res:
                for letter in digitsmap[digit]:
                    combinations.append(combination + letter)
            res = combinations
            
        return res