def nextLargerNodes(head):
    if not head:
        return []

    def reverse(head): # 翻转链表
        cur,pre = head,None
        while cur:
            cur.next,pre,cur=pre,cur,cur.next
        return pre

    stack = []
    result = []
    head = reverse(head)
    cur = head
    while cur:
        if not stack:
            stack.append(cur.val)
        while True:
            if cur.val < stack[-1]:
                result.append(stack[-1])
                stack.append(cur.val)
                break
            else:
                stack.pop()
                if not stack:
                    result.append(0)
                    stack.append(cur.val)
                    break
        cur = cur.next
    return result[::-1]