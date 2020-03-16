class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        p = ListNode(float("-inf"))
        pre = p
        tail = p
        # 依次拿head节点
        cur = head
        while cur:
            if tail.val < cur.val:
                tail.next = cur
                tail = cur
                cur = cur.next
            else:
                # 把下一次节点保持下来
                tmp = cur.next
                tail.next = tmp
                # 找到插入的位置
                while pre.next and pre.next.val < cur.val:
                    pre = pre.next
                # 进行插入操作
                cur.next = pre.next
                pre.next = cur
                pre = p
                cur = tmp
        return p.next
