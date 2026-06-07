class Solution(object):
    def reverseWords(self, s):
        l=s.split()
        for i in xrange(len(l)):
            l[i]=l[i][::-1]
        return ' '.join(l)
        