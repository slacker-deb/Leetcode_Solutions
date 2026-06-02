class Solution(object):
    def largestAltitude(self, gain):
        alt=[0,]
        for i in range(len(gain)):
            alt.append(alt[i]+gain[i])
        return max(alt)
