class Solution(object):
    def divisorSubstrings(self, num, k):
        c=0
        n=[str(num)[i:i+k] for i in xrange(len(str(num))-k+1)]
        for i in n:
            if int(i)!=0 and num%int(i)==0:
                c+=1
        return c

        