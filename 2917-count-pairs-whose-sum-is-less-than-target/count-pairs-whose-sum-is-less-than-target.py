class Solution(object):
    def countPairs(self, nums, target):
        s=0
        for i in xrange(len(nums)):
            for j in xrange(i+1,len(nums)):
                if nums[i]+nums[j]<target:
                    s=s+1
        return s
        