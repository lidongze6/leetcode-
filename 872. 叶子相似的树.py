class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode):
        list1 = []
        list2 = []
        self.leaforder(root1, list1)
        self.leaforder(root2, list2)
        return list1 == list2

    def leaforder(self, root, list):
        if root is None:
            return
        if not root.left and not root.right:
            list.append(root.val)
            return
        self.leaforder(root.left, list)
        self.leaforder(root.right, list)


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
    root1 = stringToTreeNode("[1,2]")
    root2 = stringToTreeNode("[2,2]")

    ret = Solution().leafSimilar(root1, root2)

    out = (ret)
    print(out)


if __name__ == '__main__':
    main()
