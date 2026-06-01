class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        l=[]
        m=max(candies)
        for i in candies:
            if i+extraCandies>=m:
                l.append(True)
            else:
                l.append(False)
        return l
        