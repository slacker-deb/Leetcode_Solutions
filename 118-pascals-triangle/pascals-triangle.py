class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1]]
        m = [1]
        for _ in range(1, numRows):
            l = [1]
            for i in range(len(m) - 1):
                l.append(m[i] + m[i + 1])
            l.append(1)
            ans.append(l)
            m = l
        return ans



        