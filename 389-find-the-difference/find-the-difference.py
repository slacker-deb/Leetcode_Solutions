class Solution(object):
    def findTheDifference(self, s, t):
        l=list(t)
        for i in s:
            l.remove(i)
        return l[0]
        