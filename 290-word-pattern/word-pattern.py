class Solution(object):
    def wordPattern(self, pattern, s):
        l2=s.split()
        if len(pattern)!=len(l2):
            return False
        m1={}
        m2={}
        for a,b in zip(pattern,l2):
            if a in m1 and m1[a]!=b:
                return False
            elif b in m2 and m2[b]!=a:
                return False
            else:
                m1[a]=b
                m2[b]=a
        return True
        