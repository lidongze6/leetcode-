class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        lev=0
        res=[]
        stack=[root]
        while stack:
            next_stack=[]
            tmp=[]
            for node in stack:
                if lev%2==0:
                    tmp.append(node.val)
                else:
                    tmp.insert(0, node.val)
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            lev+=1
            res.append(tmp)
            stack=next_stack
        return res