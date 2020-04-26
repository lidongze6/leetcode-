class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        # 堆
        import heapq
        stack = []
        for l in lists:
            while l:
                heapq.heappush(stack, l.val)
                l = l.next

        p=ListNode(None)
        head=p
        while stack:
            p.next=ListNode(heapq.heappop(stack))
            p=p.next
        p.next=None
        return head.next
