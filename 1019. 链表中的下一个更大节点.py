class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode):
        stack=[]
        num=0
        res=[]
        cur=head
        while cur:
            while stack and stack[-1][0]<cur.val:
                index = stack.pop()[1]
                res[index] = cur.val

            stack.append([cur.val,num])
            num+=1
            cur=cur.next
            res.append(0)

        return res