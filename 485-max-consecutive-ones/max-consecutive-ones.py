class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        s=''.join(map(str,nums))
        l=s.split('0')
        m=0
        for i in l:
            if len(i)>m:
                m=len(i)
        return m       