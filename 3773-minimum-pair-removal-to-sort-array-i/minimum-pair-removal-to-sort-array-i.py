class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if nums ==sorted(nums):
            return 0
        c=0
        m=float('inf')
        while nums!=sorted(nums):
            m=float('inf')
            for i in range (len(nums)-1):
                if nums[i]+nums[i+1]<m:
                    m=nums[i]+nums[i+1]
                    index=i
            nums.pop(index+1)
            nums.pop(index)
            nums.insert(index,m)
            c+=1
        return c