class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        l = len(edges)
        parnt = [i for i in range(l+1)]
        rnk = [1]*(l+1)

        def parent(i):
            if parnt[i] != i:
                parnt[i] = parent(parnt[i]) 
            return parnt[i]

        def addtograph(a,b):
            par_a,par_b=parent(a),parent(b)
            if par_a == par_b:
                return False
            if rnk[par_a]>=rnk[par_b]:
                parnt[b]=par_a
                parnt[par_b]=par_a
                rnk[par_a]+=1
            else:
                parnt[a]=par_b
                parnt[par_a]=par_b
                rnk[par_b]+=1
            return True

        for x,y in edges:
            if not addtograph(x,y):
                return [x,y]

        return edges[-1]