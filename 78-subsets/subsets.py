class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        return [list(k) for r in range(len(nums)+1) for k in combinations(nums,r)]
        