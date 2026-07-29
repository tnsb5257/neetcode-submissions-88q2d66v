class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visit = set()
        moves = [[1,0],[0,1],[-1,0],[0,-1]]
        max_area=0

        def bfs(i,j):
            visit.add((i,j))
            q = collections.deque()
            q.append((i,j))
            maxi = 0
            while q:
                x,y = q.popleft()
                maxi += 1
                for dx,dy in moves:
                    a,b = x+dx,y+dy
                    if a in range(rows) and b in range(cols) and grid[a][b]==1 and (a,b) not in visit:
                        q.append((a,b))
                        visit.add((a,b))
            return maxi
            
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit and grid[i][j]==1:
                    maxi = bfs(i,j)
                    max_area = max(max_area,maxi)

        return max_area