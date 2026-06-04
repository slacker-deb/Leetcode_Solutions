class Solution(object):
    def isPerfectSquare(self, num):
        from math import sqrt
        n = sqrt(num)
        return n == int(n)
        