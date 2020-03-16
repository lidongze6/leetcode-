class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode):
        if root is None:
            return True
        return self.isSameTree(root.left, self.reverse(root.right))

    def isSameTree(self, p: TreeNode, q: TreeNode):
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val
        else:
            return False

    def reverse(self, root: TreeNode):
        if root is None:
            return root
        else:
            root.left, root.right = self.reverse(root.right), self.reverse(root.left)
        return root
