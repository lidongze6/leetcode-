class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    固定节点和
    1-2-3-4-5 ------>2-3-4-5-1
    """
    def exchangelistnode(self,head):
        p=ListNode(None)
        p.next=head
        pre, cur, fow = p, head, None

        while cur and cur.next:
            fow=cur.next
            pre.next=fow
            cur.next=fow.next
            fow.next=cur
            pre=fow
        return p.next







if __name__ == "__main__":
    i = 1
    # 链表头结点
    head = ListNode(1)
    head.next = None
    tmp = None
    cur = head
    # 构造单链表
    nums = [1, 2, 3, 4, 5,6]
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
    res=solution.exchangelistnode(head)

    print("更改后")
    cur = res
    while cur != None:
        print(cur.val)
        cur = cur.next