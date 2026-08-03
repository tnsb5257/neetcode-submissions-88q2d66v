class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        q = collections.deque()
        neighbours = collections.defaultdict(list)
        for x,y in edges:
            neighbours.setdefault(x,[]).append(y)
            neighbours.setdefault(y,[]).append(x)

        for i in neighbours[0]:
            q.append((i,0))
        visited = [0]*n
        visited[0]=1
        while q:
            node,parent = q.popleft()
            visited[node]=1
            for i in neighbours[node]:
                if i == parent:
                    continue
                if visited[i] and i != parent:
                    return False
                if not visited[i]:
                    q.append((i,node))

        return True if sum(visited) == n else False
