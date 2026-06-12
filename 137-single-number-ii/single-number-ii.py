class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in set(nums):
            d[nums.count(i)]=i
        return d[1]

        