class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        if len(jewels)>=1 and len(stones)<=50:
            c=0
            for i in jewels:
                c+=stones.count(i)
        return c