class Solution(object):
    def missingNumber(self, nums):
        for i in xrange(len(nums)+1):
            if nums.count(i)==0:
                return i