class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        t = TreeNode(None)
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        else:
            t.val = t1.val + t2.val
            t.left = self.mergeTrees(t1.left, t2.left)
            t.right = self.mergeTrees(t1.right, t2.right)
        return t
