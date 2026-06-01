class Solution(object):
    def buildArray(self, nums):
        r=[]
        for i in range(len(nums)):
            r.append(nums[nums[i]])
        return r
        