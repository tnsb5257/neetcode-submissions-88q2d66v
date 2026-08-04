class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vis = [0]*n
        ans = 0
        neighbours = collections.defaultdict(list)
        for x,y in edges:
            neighbours[x].append(y)
            neighbours[y].append(x)

        def bfs(x):
            q=collections.deque()
            q.append(x)
            while q:
                y = q.popleft()
                for i in neighbours[y]:
                    if not vis[i]:
                        vis[i]=1
                        q.append(i)

        for i in neighbours:
            if vis[i]:
                continue
            vis[i]=1
            ans += 1
            bfs(i)

        return ans + (n-sum(vis))