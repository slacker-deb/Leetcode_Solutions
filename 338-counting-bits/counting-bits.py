class Solution(object):
    def countBits(self, n):
        l=[]
        for i in xrange(n+1):
            l.append(bin(i).count('1'))
        return l


        