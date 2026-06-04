class Solution(object):
    def isHappy(self, n):
        seen = set()
        def happy(n):
            r = 0
            for i in str(n):
                r += int(i) ** 2
            return r
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = happy(n)
        return True