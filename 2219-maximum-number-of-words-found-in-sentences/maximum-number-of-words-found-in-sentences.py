class Solution(object):
    def mostWordsFound(self, sentences):
        c=[]
        for i in sentences:
            l=i.split()
            c.append(len(l))
            l=[]
        return max(c)

        