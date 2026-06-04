class Solution(object):
    def reverseBits(self, n):
        z=bin(n)[2:]
        z=z.zfill(32)
        z=z[::-1]
        return(int(z,2))
        