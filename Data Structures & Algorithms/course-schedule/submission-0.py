class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        outgoing={}
        incoming = {}
        for x,y in prerequisites:
            outgoing.setdefault(x,[]).append(y)
            incoming.setdefault(y,[]).append(x)
            
        indegree = [0]*numCourses

        for x in incoming:
            indegree[x] = len(incoming[x])
        
        q = collections.deque()

        for x in range(numCourses):
            if indegree[x]==0:
                q.append(x)

        while q:
            a = q.popleft()
            if a not in outgoing:
                continue
            for x in outgoing[a]:
                indegree[x] -= 1
                if indegree[x]==0:
                    q.append(x)
        
        return True if indegree == [0]*numCourses else False

        

        

