import math
class Solution(object):
    def getSum(self, a, b):
        if -1000 <= a <= 1000 and -1000 <= b <= 1000:
            m=(pow(2,a))*(pow(2,b))
            n=int(log(m,2))
        return n