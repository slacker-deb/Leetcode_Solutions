# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m=[]
        curr=head
        while curr:
            m.append(curr.val)
            curr=curr.next
        m.sort()
        dummy=ListNode(0)
        c=dummy
        for value in m:
            c.next=ListNode(value)
            c=c.next
        return dummy.next
        