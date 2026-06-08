# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        l=[]
        curr=head
        while curr!=None:
            l.append(curr.val)
            curr=curr.next
        return l==l[::-1]        