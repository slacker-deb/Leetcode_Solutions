class Solution(object):
    def createTargetArray(self, nums, index):
        target=[]
        for i in xrange(len(nums)):
            target.insert(index[i],nums[i])
        return target
        
        