class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rnk = [1]*n
        ans = n

        def parnt(a):
            if parent[a]==a:
                return a
            temp = a
            while parent[temp] != temp:
                temp = parent[temp]
            parent[a] = temp
            return temp

        def union(a,b):
            par_a,par_b = parnt(a),parnt(b)
            if par_a == par_b:
                return False
            if rnk[par_a] > rnk[par_b]:
                parent[par_b]=par_a
                rnk[par_a]+=rnk[par_b]
            else:
                parent[par_a]=par_b
                rnk[par_b]+=rnk[par_a]
            return True

        for x,y in edges:
            components_changed=union(x,y)
            ans = ans - 1 if components_changed else ans

        return ans