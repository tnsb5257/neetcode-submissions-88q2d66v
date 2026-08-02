class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        pq = collections.deque()
        aq = collections.deque()
        ps = set()
        ats = set()
        directions = [[-1,0],[0,-1],[1,0],[0,1]]

        # push intital pacific cells to pq and atlanctic to aq
        for i in range(n):
            pq.append((0,i))
            aq.append((m-1,i))
        for i in range(m):
            pq.append((i,0))
            aq.append((i,n-1))

        def bfs(q,set_no):
            our_set = ps if set_no == 0 else ats
            other_set = ats if set_no == 0 else ps
            while q:
                x,y = q.popleft()
                our_set.add((x,y))
                for dx,dy in directions:
                    a,b = x+dx,y+dy
                    if a in range(m) and b in range(n) and heights[a][b] >= heights[x][y] and (a,b) not in our_set:
                        q.append((a,b))
                        our_set.add((a,b))
                        
        bfs(pq,0)
        bfs(aq,1)
        res=[]
        common = ps & ats
        for x,y in common:
            res.append([x,y])
        return res


