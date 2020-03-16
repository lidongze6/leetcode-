class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        p = ListNode(float("-inf"))
        p.next = head

        if not head or not head.next:
            return head

        cur = head.next
        pre, tail = head, cur  # 记录截断的位置
        while cur:
            tail=cur.next
            pre.next = tail
            cur.next=None
            p1, p2 = p, p.next  # p1,p2记录要插入的位置
            while p2 != tail and p2.val <= cur.val:
                p1 = p1.next
                p2 = p2.next
            p1.next = cur
            cur.next = p2
            if cur.next==tail:
                pre=cur
            cur=tail

        return p.next


if __name__ == "__main__":
    i=1
    #链表头结点
    head = ListNode(-1)
    head.next = None
    tmp = None
    cur= head
    # 构造单链表
    nums=[-1,5,3,4,0]
    for i in range(1,len(nums)):
        tmp = ListNode(nums[i])
        tmp.next=None
        cur.next=tmp
        cur=tmp

    print("更改前")
    cur = head
    while cur != None:
        print(cur.val)
        cur = cur.next

    solution=Solution()
    solution.insertionSortList(head)

    print("更改后")
    cur = head
    while cur != None:
        print(cur.val)
        cur = cur.next




