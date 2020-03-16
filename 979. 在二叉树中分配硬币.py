class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distributeCoins(self, root):
        if root is None:
            return 0
        self.step = 0
        self.dfs(root)
        return self.step

    def dfs(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val - 1
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.step += abs(left) + abs(right)
        return root.val + left + right - 1
