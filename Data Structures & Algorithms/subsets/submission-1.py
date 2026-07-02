class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr=[]
        l = len(nums)
        def dfs(i):
            if i >= l:
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i+1)

            curr.pop()
            dfs(i+1)
        
        dfs(0)
        return res