class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        curr = []
        l = len(candidates)
        def findComb(i,curr,target):
            if target==0:
                res.append(curr.copy())
                return
            if i==l:
                return
            if candidates[i] <= target:
                curr.append(candidates[i])
                findComb(i+1,curr,target-candidates[i])
                curr.pop()
            while i <= l-2 and candidates[i+1] == candidates[i]:
                i=i+1
            findComb(i+1,curr,target)
        
        findComb(0,curr,target)
        return res    

                