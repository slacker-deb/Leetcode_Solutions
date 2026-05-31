class Solution(object):
    def isValid(self, s):
        d = {'(': ')', '{': '}', '[': ']'}      
        if len(s) % 2 != 0:
            return False
        l = list(s)
        while len(l) > 0:
            c = len(l)
            for i in range(len(l) - 1):
                if l[i] in d and d[l[i]] == l[i + 1]:
                    l.pop(i)
                    l.pop(i)
                    break
            if c == len(l):
                return False
        return True