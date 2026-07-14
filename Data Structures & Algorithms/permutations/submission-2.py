class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr=[]
        used=set()
        l = len(nums)
        def findperm(curr,used):
            if len(curr)==l:
                ans.append(curr.copy())
                return
            for num in nums:
                if num in used:
                    continue
                curr.append(num)
                used.add(num)
                findperm(curr,used)
                curr.pop()
                used.remove(num)

        findperm(curr,used)
        return ans
