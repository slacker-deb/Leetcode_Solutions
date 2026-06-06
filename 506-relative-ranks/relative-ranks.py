class Solution(object):
    def findRelativeRanks(self, score):
        ans = [""] * len(score)
        order = sorted(range(len(score)), key=lambda i:score[i],reverse=True)
        for rank, idx in enumerate(order):
            if rank == 0:
                ans[idx] = "Gold Medal"
            elif rank == 1:
                ans[idx] = "Silver Medal"
            elif rank == 2:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(rank + 1)
        return ans