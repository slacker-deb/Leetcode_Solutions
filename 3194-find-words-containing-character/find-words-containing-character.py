class Solution(object):
    def findWordsContaining(self, words, x):
        l=[]
        for i in xrange(len(words)):
            if x in words[i]:
                l.append(i)
        return l
        