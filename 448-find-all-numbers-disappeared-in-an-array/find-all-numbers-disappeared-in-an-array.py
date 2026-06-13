class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        k=[]
        l=range(1, len(nums) + 1)
        num=set(nums) 
        for i in l:
            if i not in num:
                k.append(i)
        return k