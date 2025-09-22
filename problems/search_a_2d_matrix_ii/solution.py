class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            current_value = matrix[row][col]

            if current_value == target:
                return True
            elif current_value > target:
                col -= 1
            else:
                row += 1
        
        return False