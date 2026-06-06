class Solution(object):
    def leftRightDifference(self, nums):
        l = 0
        t = sum(nums)
        a = []
        for i in xrange(len(nums)):
            r = t- l-nums[i]
            a.append(abs(l - r))
            l+=nums[i]
        return a




        

                
        