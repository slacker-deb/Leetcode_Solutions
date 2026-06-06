class Solution(object):
    def firstUniqChar(self, s):
        freq = {}
        for a in s:
            freq[a] = freq.get(a, 0) + 1
        for i, a in enumerate(s):
            if freq[a] == 1:
                return i
        return -1
        