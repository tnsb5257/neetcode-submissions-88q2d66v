# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0

        def height(node):
            nonlocal dia
            if not node:
                return 0
            lefth,righth = height(node.left),height(node.right)
            dia = max(dia,lefth + righth)

            return 1+max(lefth,righth)

        height(root)
        return dia


