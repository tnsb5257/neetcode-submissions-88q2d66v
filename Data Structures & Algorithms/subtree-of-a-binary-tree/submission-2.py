# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def check(self,p,q):
        if p==None and q==None:
            return True
        elif p==None or q == None:
            return False
        else:
            return (p.val==q.val) and self.check(p.left,q.left) and self.check(p.right,q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root==None and subRoot==None:
            return True
        elif root==None or subRoot == None:
            return False
        else:
            return self.check(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)