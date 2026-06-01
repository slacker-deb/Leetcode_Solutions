class Solution(object):
    def maximumWealth(self, accounts):
        l=[]
        r=0
        for i in range (len(accounts)):
            for j in range(len(accounts[0])):
                r+=accounts[i][j]
            l.append(r)
            r=0
        return max(l)

        