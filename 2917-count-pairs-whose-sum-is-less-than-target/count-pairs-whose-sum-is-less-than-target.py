class Solution(object):
    def countPairs(self, nums, target):
        nums.sort()
        l,r,c=0,len(nums)-1,0
        while l<r:
            t=nums[l]+nums[r]
            if t<target:
                c+=(r-l)
                l+=1
            else:
                r-=1
        return c

        