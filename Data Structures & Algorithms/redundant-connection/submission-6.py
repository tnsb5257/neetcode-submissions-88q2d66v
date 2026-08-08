class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        canReach = collections.defaultdict(set)

        def unite(a,b):
            canReach[a].add(b)
            canReach[b].add(a)
            for i in canReach[a]:
                if i!=b:
                    canReach[b].add(i)
                    canReach[i].add(b)
            for j in canReach[b]:
                if j!= a:
                    canReach[a].add(j)
                    canReach[j].add(a)

        for x,y in edges:
            if (canReach[x] & canReach[y]):
                return [x,y]
            else:
                unite(x,y)

        return edges[-1]