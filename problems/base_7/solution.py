class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        sevenstr=""
        if num<0:
            num=abs(num)
            sevenstr+="-"
        while num>0:
            sevenstr+=str(num%7)
            num=num//7
        if sevenstr[0]=="-":
            return f"-{sevenstr[len(sevenstr):0:-1]}"
        else:
            return sevenstr[::-1]