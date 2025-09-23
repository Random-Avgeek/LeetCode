class Solution:
    def reverse(self, x: int) -> int:
        numstr=str(x)
        numrevstr=numstr[::-1]
        revnum=""
        for i in range(0,len(numrevstr)):
            if len(revnum)==0 and numrevstr[i]=="0":
                pass
            else:
                if i==len(numrevstr)-1 and numrevstr[i]=="-":
                    continue
                else:
                    revnum+=numrevstr[i]
        if (len(revnum)==0):
            revnum="0"
        revnum=int(revnum)
        if numstr[0]=="-":
            revnum=0-revnum
        if (revnum>2**31 or revnum<(-2**(31)-1)):
            return 0
        else:
            return revnum