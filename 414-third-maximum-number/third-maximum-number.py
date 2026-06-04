class Solution(object):
    def thirdMax(self, nums):
        s=set(nums)
        if len(s)<3:
            return(max(s))
        else:
            k=list(s)
            k.sort(reverse=True)
            return k[2]
        