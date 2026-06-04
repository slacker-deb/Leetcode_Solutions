class Solution(object):
    def sortArrayByParity(self, nums):
        l=[]
        k=nums[:]
        for i in nums:
            if i%2==0:
                l.append(i)
                k.remove(i)
        return l+k

        