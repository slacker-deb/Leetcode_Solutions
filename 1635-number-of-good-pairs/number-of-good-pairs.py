class Solution(object):
    def numIdenticalPairs(self, nums):
        c=0
        for i in range (0, len(nums)-1):
            for j in range(1, len(nums)):
                if i<j and nums[i]==nums[j]:
                    c+=1
        return c

        