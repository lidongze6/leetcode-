class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode):
        flag = True

        def __isBalanced(root):
            if root is None:
                return 0
            l = __isBalanced(root.left) + 1
            r = __isBalanced(root.right) + 1
            if abs(l - r) > 1:
                nonlocal flag #注意全局变量的修改问题
                flag = False
            return max(l, r)

        __isBalanced(root)
        return flag


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


root = stringToTreeNode("[1,2,2,3,3,null,null,4,4]");

ret = Solution().isBalanced(root)
print(ret)
