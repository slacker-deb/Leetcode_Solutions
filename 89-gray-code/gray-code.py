class Solution:
    def grayCode(self, n: int) -> List[int]:
        r=[]
        for i in range(1<<n):
            r.append(i^(i>>1))
        return r
        