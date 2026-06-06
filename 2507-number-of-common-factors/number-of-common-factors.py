class Solution(object):
    def commonFactors(self, a, b):
        c=1
        for i in xrange(2,min(a,b)+1):
            if a%i==0 and b%i==0:
                c+=1
        return c
        