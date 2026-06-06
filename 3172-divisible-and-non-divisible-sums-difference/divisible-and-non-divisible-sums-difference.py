class Solution(object):
    def differenceOfSums(self, n, m):
        num1,num2=0,0
        for i in xrange(1,n+1):
            if i%m==0:
                num2+=i
            num1+=i
        return num1-(num2*2)
        