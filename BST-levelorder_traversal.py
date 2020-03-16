def levelOrder(root):
    if not root:
        return []
    res = []  # 存放结果
    stack = [root]  # 记录当前层的节点
    while stack:
        tmp = []  # 存放当前层的节点的值
        next_stack = []  # 记录下一层节点
        for node in stack:
            tmp.append(node.val)
            if node.left:
                next_stack.append(node.left)
            if node.right:
                next_stack.append(node.right)
        res.append(tmp)
        stack = next_stack
    return res
