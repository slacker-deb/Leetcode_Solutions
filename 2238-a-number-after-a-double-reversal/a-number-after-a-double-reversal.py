class Solution(object):
    def isSameAfterReversals(self, num):
        if num==0 or str(num)[-1]!='0':
            return True
        else:
            return False