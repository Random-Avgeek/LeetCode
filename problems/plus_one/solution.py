class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<9:
            digits[-1]+=1
            return digits
        elif digits[-1]==9:
            num=""
            for i in range(0,len(digits)):
                num+=str(digits[i])
            num=int(num)
            num+=1
            num=str(num)
            final=[]
            for i in range(0,len(num)):
                final.append(int(num[i]))
            return final