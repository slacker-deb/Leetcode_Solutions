class Solution(object):
    def countDigits(self, num):
        r=0
        for i in set(str(num)):
            if num%int(i)==0:
                r+=str(num).count(i)
        return r

        