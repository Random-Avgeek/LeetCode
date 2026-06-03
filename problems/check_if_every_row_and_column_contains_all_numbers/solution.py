class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        for i in range(0,len(matrix)):
            checklist=[False]*len(matrix)
            colcheck=[False]*n
            for j in range(0,n):
                if checklist[matrix[i][j]-1]==False:
                    checklist[matrix[i][j]-1]=True
            if False in checklist:
                return False
            for j in range(0,n):
                if colcheck[matrix[j][i]-1]==False:
                    colcheck[matrix[j][i]-1]=True
            if False in colcheck:
                return False
        return True