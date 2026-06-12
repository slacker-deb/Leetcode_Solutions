# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        base = l // k
        extra = l % k
        ans = []
        curr = head
        for i in range(k):
            part_head = curr
            size = base
            if extra > 0:
                size += 1
                extra -= 1
            for j in range(size - 1):
                if curr:
                    curr = curr.next
            if curr:
                nxt = curr.next
                curr.next = None
                curr = nxt
            ans.append(part_head)
        return ans