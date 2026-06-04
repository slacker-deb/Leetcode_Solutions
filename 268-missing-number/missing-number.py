class Solution(object):
    def missingNumber(self, nums):
        a=len(nums)
        for i in xrange(a):
            a^=i^nums[i]
        return a
            