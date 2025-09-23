class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")
        len1=len(v1)
        len2=len(v2)
        print(v1)
        print(v2)
        maxlen=max(len1,len2)
        for i in range(maxlen):
            if i<len1:
                num1=int(v1[i])
            else:
                num1=0
            if i<len2:
                num2=int(v2[i])
            else:
                num2=0
            if num1>num2:
                return 1
            elif num1<num2:
                return -1
            else:
                if i==maxlen-1:
                    return 0
                else:
                    continue
        return 0