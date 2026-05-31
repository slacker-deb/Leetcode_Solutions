class Solution(object):
    def reverse(self, x):
        s=str(abs(x))
        s=s[::-1]
        s=int(s)
        if s>(2**31)-1:
            return 0
        else: 
            if x<0:
                return (s*(-1))
            else:
                return s

        