class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode):
        # 自上而下，速度稍慢
        if root is None:
            return True
        else:
            return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and self.isBalanced(
                root.left) and self.isBalanced(root.right)

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


