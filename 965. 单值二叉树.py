class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def __isUnivalTree(root, target):
            if root is None:
                return True
            if root.val != target:
                return False
            else:
                return __isUnivalTree(root.left, root.val) and __isUnivalTree(root.right, root.val)

        return __isUnivalTree(root.left, root.val) and __isUnivalTree(root.right, root.val)
