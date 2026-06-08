class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        s=0
        for i in range (len(arr)):
            k=1
            while i+k<len(arr)+1:
                s+=sum(arr[i:i+k])
                k+=2
        return s

            

        