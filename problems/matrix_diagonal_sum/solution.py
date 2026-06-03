class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        for i in range(0,len(mat)):
            for j in range(0,len(mat)):
                if i==j or j==len(mat)-i-1:
                    sum+=mat[i][j]
        return sum