class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        numshift=k%(rows*cols)
        newgrid=[[0 for _ in range(cols)] for _ in range(rows)]
        total=rows*cols
        for r in range(rows):
            for c in range(cols):
                idx=r*cols+c
                newidx=(idx+numshift)%total
                newr=newidx//cols
                newc=newidx%cols
                newgrid[newr][newc]=grid[r][c]
        return newgrid
        