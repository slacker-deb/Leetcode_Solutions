class Solution(object):
    def minElement(self, nums):
        k=[]
        l=[]
        for i in nums:
            for j in range(len(str(i))):
                l.append(i%10)
                i=i/10
            k.append(sum(l))
            l=[]
        return min(k)
            

        