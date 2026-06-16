# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(node):
            if not node:
                return 0
            
            lefth = height(node.left)
            if lefth==-1:
                return -1
            righth = height(node.right)
            if righth==-1:
                return -1
            
            if abs(lefth-righth)>1:
                return -1
            return 1+max(lefth,righth)

        return height(root) != -1
