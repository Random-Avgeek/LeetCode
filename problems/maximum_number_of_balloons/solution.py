class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        minnum={'b':1,'a':1,'l':2,'o':2,'n':1}
        instances={'b':0,'a':0,'l':0,'o':0,'n':0}
        for char in text:
            if char == 'b':
                instances[char]+=1
            elif char == 'a':
                instances[char]+=1
            elif char == 'l':
                instances[char]+=1
            elif char == 'o':
                instances[char]+=1
            elif char == 'n':
                instances[char]+=1
        return min(instances['b']//minnum['b'],instances['a']//minnum['a'],instances['l']//minnum['l'],instances['o']//minnum['o'],instances['n']//minnum['n'])