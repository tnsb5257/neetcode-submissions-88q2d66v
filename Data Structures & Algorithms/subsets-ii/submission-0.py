class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()
        l = len(nums)
        def dfs(i):
            if i == l:
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i+1)

            curr.pop()
            while i<=l-2 and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)

        dfs(0)
        return res
            
            