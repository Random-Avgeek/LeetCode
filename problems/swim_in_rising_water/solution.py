class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        left = grid[0][0]
        right = n * n

        def canReach(t):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visited = set()
            stack = [(0, 0)]
            while stack:
                r, c = stack.pop()
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                for dir in directions:
                    dr = dir[0]
                    dc = dir[1]
                    nr = r + dr
                    nc = c + dc
                    if (
                        0 <= nr < n
                        and 0 <= nc < n
                        and (nr, nc) not in visited
                        and grid[nr][nc] <= t
                    ):
                        stack.append((nr, nc))
            return (n - 1, n - 1) in visited

        while left < right:
            mid = (left + right) // 2
            if canReach(mid):
                right = mid
            else:
                left = mid + 1
        return left
