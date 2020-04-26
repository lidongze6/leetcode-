# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        # 分治法
        l = len(lists)

        def merge(l1, l2):
            if not l1: return l2
            if not l2: return l1

            if l1.val <= l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2

        if l == 1: return lists[0]
        if l == 2: return merge(lists[0], lists[1])
        if l > 2:
            mid = l // 2
            left = self.mergeKLists(lists[:mid])
            right = self.mergeKLists(lists[mid:])
            return merge(left, right)
