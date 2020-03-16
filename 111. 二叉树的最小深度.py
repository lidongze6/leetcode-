class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode):
        return self.__minDepth(root)

    def __minDepth(self, root):
        if root is None:
            return 0
        elif root.left and root.left:
            return min(self.__minDepth(root.left), self.__minDepth(root.right)) + 1
        else:
            return self.__minDepth(root.left)+1 if root.left else self.__minDepth(root.right)+1