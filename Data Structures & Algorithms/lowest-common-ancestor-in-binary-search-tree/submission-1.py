# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        low, high = min(p.val, q.val), max(p.val, q.val)
        if root and root.val >= low and root.val <= high:
            return root
        if root and root.val > high:
            a = self.lowestCommonAncestor(root.left, p, q)
            return a
        if root and root.val < low:
            b = self.lowestCommonAncestor(root.right, p, q)
            return b
        return root
