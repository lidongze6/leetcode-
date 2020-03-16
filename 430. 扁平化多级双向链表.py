class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node):
        def dfs(head):
            if head is None:
                return head
            p = head
            pre = head.next
            if p.child:
                tail = dfs(p.child)
                p.next = tail
                tail.prev = p
                p.child = None
                while p.next:
                    p = p.next
                p.next = pre
            if pre:
                pre = dfs(pre)
                pre.prev = p
            return head
        dfs(head)
        return head
