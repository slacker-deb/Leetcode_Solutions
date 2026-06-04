class Solution(object):
    def plusOne(self, digits):
        d=0
        r=[]
        for i in digits:
            d=(d*10)+i
        d+=1
        for i in xrange(len(str(d))):
            r=[d%10]+r
            d=d//10
        return r


        