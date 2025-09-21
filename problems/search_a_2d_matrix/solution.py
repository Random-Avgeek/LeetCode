class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows=len(matrix)
        ncol=len(matrix[0])
        for i in  range(nrows):
            if i!=nrows-1:
                if matrix[i][-1]<target:
                    i+=1
                else:
                    for j in range(ncol):
                        if matrix[i][j]==target:
                            return True
            else:
                if matrix[i][-1]<target:
                    return False
                else:
                    for j in range(ncol):
                        if matrix[i][j]==target:
                            return True
        return False