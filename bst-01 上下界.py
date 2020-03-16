class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.__left = left
        self.__right = right


class BST:
    def __init__(self, root):
        self.__root = root

    # 查找
    def search(self, target):
        return self.__search(self.__root, target)

    def __search(self, node, target):
        if node is None:
            return None
        if target == node.item:
            return node.item
        elif target > node.item:
            return self.__search(node.__right, target)
        else:
            return self.__search(node.__left, target)

    # 插入
    def inser(self, value):
        self.__root = self.__insert(self.__root, value)

    def __insert(self, node, value):
        if node is None:
            return Node(value)
        if value == node.item:
            pass
        elif value > node.item:
            node.__right = self.__insert(node.__right, value)
        else:
            node.__left = self.__insert(node.__left, value)
        return node  # 非常重要的，不能没有，相当于将插入后的次节点进行更新，类似于root（旧，没有插入前）= root（新，有新的插入值后）

    # 删除
    def remove(self, value):
        self.__root = self.__remove(self.__root, value)

    def __remove(self, node, value):
        if node is Node:
            return None
        if node.item > value:
            node.__left = self.__remove(node.__left, value)
        elif node.item < value:
            node.__right = self.__remove(node.__right, value)
        else:
            if node.__left is None:
                node = node.__left
            elif node.__right is Node:
                node = node.__right
            else:
                node.__item = self.__getmax(node.__left)
                node.left = self.__remove(node.__left, node.__item)
        return node

    # 获取最大值
    def getmax(self):
        return self.__getmax(self.__root)

    # 获取当前节点最大值
    def __getmax(self, node):
        if node.__right is None:
            return node.__item
        else:
            return self.__getmax(node.__right)

    # 获取最小值
    def getmin(self):
        return self.__getmin(self.__root)

    # 获取当先节点最小值
    def __getmin(self, node):
        if node.__left is None:
            return node.__item
        else:
            return self.__getmax(node.__left)

    # 获取下界
    def floor(self, root, target):
        if root is None:
            return None
        else:
            if root.val == target:
                return target
            elif root.val > target:
                return self.floor(root.left, target)
            else:
                tmp = root
                # 以右节点为根节点的子树中寻找下界的结果，若返回的是空，证明没找到,否则证明找到了，
                # 而根据bst的性质右子树下面的值一定比根节点大，而又找到了target的下界，则断定肯定是答案
                res = self.floor(root.right, target)
                if res is None:
                    return tmp.val
                else:
                    return res.val

    # 获取上界
    def ceiling(self,root,target):
        if root is None:
            return None
        else:
            if root.val == target:
                return target
            elif root.val < target:
                return self.ceiling(root.right, target)
            else:
                tmp = root
                # 以左节点为根节点的子树中寻找上界的结果，若返回的是空，证明没找到,否则证明找到了，
                # 而根据bst的性质左子树下面的值一定比根节点小，而又找到了target的上界，则断定肯定是答案
                res = self.ceiling(root.left, target)
                if res is None:
                    return tmp.val
                else:
                    return res.val

