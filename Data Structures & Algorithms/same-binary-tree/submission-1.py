# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self,p,q):
        if p == None and q == None:
            return  True
        elif p == None or q == None:
            return False
        else:
            return (p.val == q.val) and self.check(p.left,q.left) and self.check(p.right,q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check(p,q)
                
