class Solution(object):
    def sumBase(self, n, k):
        a=0
        while n:
            a+=n%k
            n//=k

        return a

