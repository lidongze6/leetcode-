class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 循环
        if not l1: return l2
        if not l2: return l1
        p = ListNode(None)
        p1, p2 = l1, l2
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if not p1:
            p.next = p2
        if not p2:
            p.next = p1
        return l1 if l1.val <= l2.val else l2
