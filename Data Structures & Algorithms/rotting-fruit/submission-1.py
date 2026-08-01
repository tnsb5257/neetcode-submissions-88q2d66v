class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r,c = len(grid),len(grid[0])
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        q = collections.deque()
        min_time = 0
        total_fruits=0
        rotten_fruits=0
        for row in range(r):
            for col in range(c):
                if grid[row][col] == 1:
                    total_fruits +=1
                if grid[row][col] == 2:
                    q.append((row,col,0))
                    rotten_fruits +=1
                    total_fruits +=1
        
        while q:
            x,y,batch = q.popleft()
            min_time = max(min_time, batch)
            for dx,dy in directions:
                a,b = x+dx,y+dy
                if a in range(r) and b in range(c) and grid[a][b] == 1:
                    grid[a][b] = 2
                    q.append((a,b,batch+1))
                    rotten_fruits += 1
        if rotten_fruits != total_fruits:
            return -1
        return min_time