class Solution(object):
    def subtractProductAndSum(self, n):
        n=str(n)
        m=1
        a=0
        for i in n:
            m*=int(i)
            a+=int(i)
        return (m-a)
            
        