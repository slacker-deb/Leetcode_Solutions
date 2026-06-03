class Solution(object):
    def isPalindrome(self, s):
        l=''
        s=s.lower()
        k='abcdefghijklmnopqrstuvwxyz0123456789'
        for i in s:
            if i in k:
                l+=i
        return l==l[-1::-1]     