# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findgood(self,node,mx):
        if not node:
            return 0
        if node.val < mx:
            return self.findgood(node.left,mx)+self.findgood(node.right,mx)
        return 1+self.findgood(node.left,node.val)+self.findgood(node.right,node.val)

    def goodNodes(self, root: TreeNode) -> int:
        return 1+self.findgood(root.left,root.val)+self.findgood(root.right,root.val)