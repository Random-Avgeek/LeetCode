class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * (n + 1) for _ in range(n + 1)]
        for row1, col1, row2, col2 in queries:
            matrix[row1][col1] += 1
            if col2 + 1 < n:
                matrix[row1][col2 + 1] -= 1
            if row2 + 1 < n:
                matrix[row2 + 1][col1] -= 1
            if row2 + 1 < n and col2 + 1 < n:
                matrix[row2 + 1][col2 + 1] += 1
        for i in range(n):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
        for j in range(n):
            for i in range(1, n):
                matrix[i][j] += matrix[i - 1][j]
        return [row[:n] for row in matrix[:n]]