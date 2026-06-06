class Solution(object):
    def differenceOfSums(self, n, m):
        num1,num2=0,0
        for i in xrange(1,n+1):
            num1+=i
        if n<m:
            return num1
        else:
            for i in xrange(m,n+1,m):
                num2+=i
            return num1-(num2*2)
        