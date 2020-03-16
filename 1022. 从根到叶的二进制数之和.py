class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, tmp, res):
            if root is None:
                return
            if not root.left and not root.right:
                nonlocal res
                res += tmp * 2 + root.val
            else:
                dfs(root.left, tmp * 2 + root.val, res)
                dfs(root.right, tmp * 2 + root.val, res)

        dfs(root, 0, res)
        return res
