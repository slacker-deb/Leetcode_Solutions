class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = list1
        end = list1       
        for i in range(a - 1):
            start = start.next           
        for i in range(b):
            end = end.next            
        list2_tail = list2
        while list2_tail.next:
            list2_tail = list2_tail.next            
        start.next=list2
        list2_tail.next=end.next
        return list1

        