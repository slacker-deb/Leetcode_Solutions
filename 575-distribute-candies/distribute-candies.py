class Solution(object):
    def distributeCandies(self, candyType):
        s=set(candyType)
        return min(len(s),len(candyType)//2)
        