class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        R, C = len(heightMap), len(heightMap[0])
        if R < 3 or C < 3: return 0
        
        heap = []
        visited = [[False] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True
        
        volume = 0
        max_height = 0
        
        while heap:
            h, r, c = heapq.heappop(heap)
            max_height = max(max_height, h)
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                    visited[nr][nc] = True
                    neighbor_h = heightMap[nr][nc]
                    
                    if neighbor_h < max_height:
                        volume += max_height - neighbor_h
                    heapq.heappush(heap, (neighbor_h, nr, nc))
                    
        return volume