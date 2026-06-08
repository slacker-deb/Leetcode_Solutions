# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow=head
        fast=head
        check=False
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                check=True
                break
        if not (check):
            return None
        l=1
        while slow.next!=fast:
            slow=slow.next
            l+=1
        slow=head
        fast=head
        for i in range(l):
            fast=fast.next
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow

        