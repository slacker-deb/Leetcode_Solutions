class Solution(object):
    def totalMoney(self, n):
        m=0
        w=1
        while n>0:
            for day in xrange(min(7, n)):
                m+= w+day
            w+=1
            n-=7
        return m
        




        