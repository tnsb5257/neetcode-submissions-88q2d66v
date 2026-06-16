# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxd(self,root):
        if not root:
            return 0
        return 1+max(self.maxd(root.left),self.maxd(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        dia = 0
        while q:
            node = q.popleft()
            dia = max(dia,self.maxd(node.left)+self.maxd(node.right))
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return dia