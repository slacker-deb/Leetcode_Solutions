class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex+1 == 1:
            return [1]
        m = [1]
        for _ in range(1, rowIndex+1):
            l = [1]
            for i in range(len(m) - 1):
                l.append(m[i] + m[i + 1])
            l.append(1)
            m = l
        return m
        