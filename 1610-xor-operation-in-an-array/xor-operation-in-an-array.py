class Solution(object):
    def xorOperation(self, n, start):
        x=0
        for i in range(n):
            x^=(start+i*2)
        return x
        