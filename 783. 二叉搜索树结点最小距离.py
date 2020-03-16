class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res=self.inorder(root)
        return min([res[i]-res[i-1] for i in range(1,len(res))])

    def inorder(self,root):
        if root is None:
            return []
        return self.inorder(root.left)+[root.val]+self.inorder(root.right)