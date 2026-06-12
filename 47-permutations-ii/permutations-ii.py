class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        import itertools
        unique_perms = set(itertools.permutations(nums))
        return [list(p) for p in unique_perms]
        
        