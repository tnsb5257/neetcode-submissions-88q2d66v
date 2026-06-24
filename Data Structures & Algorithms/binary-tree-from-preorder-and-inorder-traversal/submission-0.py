# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode()
        root.val = preorder[0]
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                root_pos = i
        root.left = self.buildTree(preorder[1:root_pos+1],inorder[:root_pos])
        root.right = self.buildTree(preorder[root_pos+1:],inorder[root_pos+1:])
        return root
            