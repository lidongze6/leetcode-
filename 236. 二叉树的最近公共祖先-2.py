class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic = {root: None}

        def dfs(root):
            if not root:
                return
            if root.left:
                dic[root.left] = root
                dfs(root.left)
            if root.right:
                dic[root.right] = root
                dfs(root.right)
            return

        dfs(root)
        l1, l2 = p, q
        while l1 != l2:
            # 此处相当于相交链表的问题，A+B=B+A 类似leetcode160
            l1 = dic.get(l1, q)
            l2 = dic.get(l2, p)
        return l1
