class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        if not root:
            return root
            # 转为set查找更快
        to_delete = set(to_delete)
        # 存放答案
        ans = []
        # 存放需要搜索的节点
        del_node = [root]

        def dfs(root):
            # 节点是删除节点时
            if root.val in to_delete:
                # 如果节点有左右子节点，存入del_node
                if root.left:
                    del_node.append(root.left)
                if root.right:
                    del_node.append(root.right)
                # false表示是删除节点
                return False
            # 对左子树进行搜索
            if root.left:
                res = dfs(root.left)
                # 如果左子树是删除节点，则将左子树设置为None
                if not res:
                    root.left = None
            # 对右子树进行搜索
            if root.right:
                res = dfs(root.right)
                # 如果右子树是删除点解，则将右子树设置为None
                if not res:
                    root.right = None
            return True

        # 将所有点进行遍历
        while len(del_node) > 0:
            node = del_node.pop(0)
            # 只有该点不是删除节点的时候才添加到ans中
            if dfs(node):
                ans.append(node)
        return ans
