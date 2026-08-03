class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        outgoing = {}
        indegree = [0]*numCourses
        res = []
        tracked = 0
        q = collections.deque()
        for x,y in prerequisites:
            outgoing.setdefault(y,[]).append(x)
            indegree[x]+=1
        
        for i,x in enumerate(indegree):
            if x == 0:
                q.append(i)
            
        if not q:
            return []

        while q:
            x = q.popleft()
            res.append(x)
            tracked += 1
            if x not in outgoing:
                continue
            for y in outgoing[x]:
                indegree[y] -= 1
                if indegree[y]==0:
                    q.append(y)
        
        return res if tracked == numCourses else []
        