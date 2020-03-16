class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseKGroup(head,k):
    dummy = ListNode(None)
    dummy.next = head

    cur = head
    fow = dummy
    ret = fow
    for i in range(k):
        if fow.next:
            fow = fow.next
        else:
            return head

    while True:
        pre = None
        fow = cur
        for j in range(k):
            pre, pre.next, cur = cur, pre, cur.next
        fow.next = cur
        ret.next = pre
        ret = fow
        for i in range(k):
            if fow.next:
                fow = fow.next
            else:
                return dummy.next
