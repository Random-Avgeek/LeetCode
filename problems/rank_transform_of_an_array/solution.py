class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp=sorted(set(arr))
        index={}
        for i in range(len(temp)):
            index[temp[i]]=i+1
        for i in range(len(arr)):
            if arr[i] in index:
                arr[i]=index[arr[i]]
        return arr