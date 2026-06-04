class Solution(object):
    def totalWaviness(self, num1, num2):
        w=0
        for i in xrange (num1,num2+1):
            x=str(i)
            if len(x)<3:
                w+=0
            else:
                for j in xrange (1,len(x)-1):
                    if x[j-1]<x[j]>x[j+1] or x[j-1]>x[j]<x[j+1]:
                        w+=1
        return w


        