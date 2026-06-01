class Solution(object):
    def runningSum(self, nums):
        r=[]
        s=0
        for i in range (len(nums)):
            for j in range(i+1):
                s+=nums[j]
            r.append(s)
            s=0
        return r

        