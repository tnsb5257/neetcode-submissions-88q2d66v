class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 -1
        m,n = len(grid),len(grid[0])
        directions = [[-1,0],[0,-1],[1,0],[0,1]]

        def bfs(k,l):
            q = collections.deque()
            q.append((k,l))
            while q:
                x,y = q.popleft()
                for dx,dy in directions:
                    a,b = x+dx,y+dy
                    if a in range(m) and b in range(n) and grid[a][b] != -1:
                        if grid[a][b]>grid[x][y]+1:
                            grid[a][b]=grid[x][y]+1
                            q.append((a,b))
            return

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    bfs(r,c)
        return