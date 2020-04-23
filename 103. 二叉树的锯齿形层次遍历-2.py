class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        lev = 0
        res = [[]]

        def levelOrderhelper(root, lev, res):
            if root is None:
                return
            if lev % 2 == 0:
                res[lev].append(root.val)
            else:
                res[lev].insert(0, root.val)
            if lev + 1 == len(res):
                if root.left or root.right:
                    res.append([])
            levelOrderhelper(root.left, lev + 1, res)
            levelOrderhelper(root.right, lev + 1, res)

        levelOrderhelper(root, lev, res)
        return res
