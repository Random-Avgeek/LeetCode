class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        
        pac = set()
        at = set()

        def dfs(row, col, oc):
            if (row, col) in oc:
                return
            
            oc.add((row, col))

            for row_diff, col_diff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row, next_col = row + row_diff, col + col_diff
                
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if heights[next_row][next_col] >= heights[row][col]:
                        dfs(next_row, next_col, oc)

        for col in range(cols):
            dfs(0, col, pac)
        for row in range(rows):
            dfs(row, 0, pac)

        for col in range(cols):
            dfs(rows - 1, col, at)
        for row in range(rows):
            dfs(row, cols - 1, at)

        result = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pac and (row, col) in at:
                    result.append([row, col])
                    
        return result