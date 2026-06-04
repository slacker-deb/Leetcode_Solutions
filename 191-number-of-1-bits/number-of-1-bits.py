class Solution(object):
    def hammingWeight(self, n):
        n=bin(n)[2:]
        return n.count('1')
        