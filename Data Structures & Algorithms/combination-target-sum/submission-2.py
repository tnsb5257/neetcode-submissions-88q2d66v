class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        l = len(nums)
        def findComb(i,curr,target):
            if target == 0:
                res.append(curr.copy())
                return
            if i == l:
                return
            if nums[i] <= target:
                curr.append(nums[i])
                findComb(i,curr,target-nums[i])
                curr.pop()
            findComb(i+1,curr,target)

        findComb(0,curr,target)
        return res