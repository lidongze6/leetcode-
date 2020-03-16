class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res = []

        def sum2(root):
            if root is None:
                return
            if L <= root.val <= R:
                res.append(root.val)
                sum2(root.left)
                sum2(root.right)
            elif root.val > R:
                sum2(root.left)
            elif root.val < L:
                sum2(root.right)

        sum2(root)
        return sum(res)



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


def main():
    root = stringToTreeNode("[10,5,15,3,7,null,18]")

    ret = Solution().rangeSumBST(root,7,15)

    out = (ret)
    print(out)


if __name__ == '__main__':
    main()