class Solution:
    def findTheDifference(self, s, t):
        for i in t:
            if t.count(i) != s.count(i):
                return i