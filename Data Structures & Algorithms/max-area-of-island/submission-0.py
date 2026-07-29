class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visit = set()
        moves = [[1,0],[0,1],[-1,0],[0,-1]]
        max_area=0
        def dfs(x,y):
            if x<0 or y<0 or x>=rows or y>=cols or grid[x][y] == 0:
                return 0
            if (x,y) in visit:
                return 0
            cnt = 0
            visit.add((x,y))
            for dx,dy in moves:
                a,b=x+dx,y+dy
                if a in range(rows) and b in range(cols) and grid[a][b]==1 and (a,b) not in visit:
                    cnt += dfs(a,b)
                    
            return 1 + cnt

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit and grid[i][j]==1:
                    maxi = dfs(i,j)
                    max_area = max(max_area,maxi)

        return max_area