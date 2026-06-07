class Solution(object):
    def mergeAlternately(self, word1, word2):
        s = ''
        m = min(len(word1), len(word2))
        for i in xrange(m):
            s += word1[i] + word2[i]
        s += word1[m:]
        s += word2[m:]
        return s