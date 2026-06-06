class Solution(object):
    def numberOfMatches(self, n):
        c=0
        while n!=1:
            if n%2==0:
                c+=n//2
                n//=2
            else:
                c+=(n-1)//2
                n=(n+1)//2
        return c
            
        