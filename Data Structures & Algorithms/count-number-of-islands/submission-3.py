class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        moves = [[1,0],[0,1],[0,-1],[-1,0]]

        def dfs(i,j):
            if i >= rows or j >= cols or i<0 or j<0:
                return
            if grid[i][j]=="0":
                return
            if (i,j) not in visit:
                visit.add((i,j))
                for k in range(4):
                    new_pos = [x+y for x,y in zip([i,j],moves[k])]
                    new_i,new_j=new_pos
                    dfs(new_i,new_j)
            return

        rows,cols = len(grid),len(grid[0])
        visit = set()
        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visit:
                        islands+=1
                        dfs(i,j)
        
        return islands