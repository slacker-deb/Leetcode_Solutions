class Solution(object):
    def fib(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            f1=0
            f2=1
            for i in xrange(n-1):
                n=f1+f2
                f1,f2=f2,n
        return n

        
