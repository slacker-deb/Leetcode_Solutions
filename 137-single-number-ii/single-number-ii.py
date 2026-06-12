class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for key in nums:
            if key not in d:
                d[key]=1
            else:
                d[key]+=1 
        for key,value in d.items():
            if value==1:
                ans=key
        return ans
        