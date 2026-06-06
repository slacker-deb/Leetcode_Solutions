class Solution(object):
    def leftRightDifference(self, nums):
        r=[]
        for i in xrange(len(nums)):
            lsum=sum(nums[0:i])
            rsum=sum(nums[i+1:len(nums)])
            r.append(abs(lsum-rsum))
        return r



        

                
        