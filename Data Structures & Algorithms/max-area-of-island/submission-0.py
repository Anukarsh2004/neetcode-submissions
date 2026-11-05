class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        area = 0

        def bfs(r,c):
            q = deque()
            area = 1
            q.append((r,c))
            grid[r][c] = 0

            while q:
                row, col = q.popleft()
                
                for nr, nc in directions:
                    nr = row + nr
                    nc = col + nc

                    if (nr not in range(ROWS) or nc not in range(COLS) or grid[nr][nc]==0):
                        continue
                    area +=1
                    q.append((nr,nc))
                    grid[nr][nc] = 0

            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r,c))
        
        return area


    