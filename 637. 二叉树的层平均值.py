class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode):
        from collections import defaultdict
        res = defaultdict(list)

        def helper(root, res, deep):
            if root is None:
                return
            res[deep].append(root.val)
            helper(root.left, res, deep + 1)
            helper(root.right, res, deep + 1)

        helper(root, res, 0)
        value=list(res.values())
        return [sum(i)/len(i) for i in value]

