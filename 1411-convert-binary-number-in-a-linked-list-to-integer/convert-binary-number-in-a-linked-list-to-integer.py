# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr=head
        b=0
        while curr!=None:
            b=b*10+curr.val
            curr=curr.next
        return int(str(b),2)
        