class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        board=[['.']*n for _ in range(n)]

        def safe(row,column):
            for i in range(0,row):
                if board[i][column]=='Q':
                    return False
                if column - (row - i) >= 0 and board[i][column - (row - i)] == 'Q': return False
                if column + (row - i) < n and board[i][column + (row - i)] == 'Q': return False
            return True
        
        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            for column in range(n):
                if safe(row,column):
                    board[row][column]="Q"
                    backtrack(row+1)
                    board[row][column]="."
        backtrack(0)
        return result