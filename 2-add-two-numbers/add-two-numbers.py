# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dumb=ListNode(0)
        p=dumb
        c=0
        a=0
        while True:
            if l1!=None:
                b=l1.val
                l1=l1.next
            else:
                b=0
            if l2!=None:
                d=l2.val
                l2=l2.next
            else:
                d=0            
            a=b+d+c
            c=0
            if a>=10:
                c=a//10
                a=a%10
            p.next=ListNode(a)
            p=p.next
            if l1==None and l2==None:
                break
        if c>0:
            p.next=ListNode(c)
        return dumb.next
            
        