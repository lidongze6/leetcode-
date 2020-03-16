class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        p = ListNode(None)
        p.next = head
        cur = p
        self.swap(cur, cur.next, cur.next.next)
        return p.next

    def swap(self, p, p1, p2):
        if not p1 or not p2:
            return
        p1.next = p2.next
        p2.next = p1
        p.next = p2
        self.swap(p.next.next,p1.next,p1.next.next)



if __name__=="__main__":
    nums=[1,2,3,4]
    i=0
    head=ListNode(nums[i])
    cur=head
    while i<len(nums)-1:
        i+=1
        tmp = ListNode(nums[i])
        cur.next =tmp
        cur = tmp
    print("原始")
    cur=head
    while cur !=None:
        print(cur.val)
        cur= cur.next

    r = Solution()
    r.swapPairs(head)
    print("之后")
    cur = head
    while cur != None:
        print(cur.val)
        cur = cur.next