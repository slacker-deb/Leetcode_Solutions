class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        def sen(l):
            r=''
            for i in l:
                r+=i
            return r
        r1=sen(word1)
        r2=sen(word2)
        return r1==r2

        