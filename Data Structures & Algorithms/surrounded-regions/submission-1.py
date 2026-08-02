class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board),len(board[0])
        q = collections.deque()
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        safe = set()
        for i in range(m):
            if board[i][0] == 'O':
                q.append((i,0))
            if board[i][n-1] == 'O':
                q.append((i,n-1))
        for i in range(n):
            if board[0][i] == 'O':
                q.append((0,i))
            if board[m-1][i] == 'O':
                q.append((m-1,i))
        
        while q:
            x,y = q.popleft()
            safe.add((x,y))
            for dx,dy in directions:
                    a,b = x+dx,y+dy
                    if a in range(m) and b in range(n) and (a,b) not in safe:
                        if board[a][b]=='O':
                            q.append((a,b))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in safe:
                    board[i][j] = 'X'
