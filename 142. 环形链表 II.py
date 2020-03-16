class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return None
        fast = slow = head
        temp = False  # 记录是否有环
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                temp = True
                break
        if temp == True:  # 若有环，则计算环起点位置
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None  # 若temp False 则无环，返回空
