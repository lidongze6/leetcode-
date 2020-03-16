"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        p1, p2 = head,head.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        ri = p1.next
        le = head
        p1.next = None

        left=self.sortList(le)
        right=self.sortList(ri)
        res=self.merge(left, right)

        return res
    def merge(self, left, right):
        cur =p = ListNode(None)
        pleft, pright = left, right
        while pleft and pright:
            if pleft.val <= pright.val:
                cur.next,pleft = pleft,pleft.next
            else:
                cur.next,pright = pright,pright.next
            cur = cur.next
        cur.next=pleft if pleft else pright
        return p.next


if __name__ == "__main__":
    i = 1
    # 链表头结点
    head = ListNode(-1)
    head.next = None
    tmp = None
    cur = head
    # 构造单链表
    nums = [-1, 5, 3, 4, 0]
    for i in range(1, len(nums)):
        tmp = ListNode(nums[i])
        tmp.next = None
        cur.next = tmp
        cur = tmp

    print("更改前")
    cur = head
    while cur != None:
        print(cur.val)
        cur = cur.next

    solution = Solution()
    solution.sortList(head)

    print("更改后")
    cur = head
    while cur != None:
        print(cur.val)
        cur = cur.next
