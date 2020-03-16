class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) and p.val==q.val
        else:
            return False