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
            return 1+max(height(node.left),height(node.right))

        q = deque([root])
        while q:
            node = q.pop()
            if height(node.left) - height(node.right) > 1 or height(node.left) - height(node.right) <-1:
                return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return True
        