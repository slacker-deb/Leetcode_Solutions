# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        delete = set(nums)
        dummy = ListNode(0, head)
        curr = head
        prev = dummy
        while curr:
            if curr.val in delete:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next

        