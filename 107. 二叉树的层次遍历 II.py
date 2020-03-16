class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        from collections import defaultdict
        res = defaultdict(list)
        self.__levelOrderBottom(root, res, 0)
        res = res.values()
        return list(res)[::-1]

    def __levelOrderBottom(self, root, res, dept):
        if root is None:
            return
        res[dept].append(root.val)
        self.__levelOrderBottom(root.left, res, dept + 1)
        self.__levelOrderBottom(root.right, res, dept + 1)

## 其实可以直接用列表，到第几层直接就res[dept]=root.val 即可
