class Solution(object):
    def isPalindrome(self, x):
        check=x
        d=0
        while check>0:
            digit=check%10
            d=d*10+digit
            check=check//10
        if x==d:
            return True
        else:
            return False
        