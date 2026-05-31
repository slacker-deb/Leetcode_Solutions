class Solution(object):
    def romanToInt(self, s):
        r=0
        l=list(s[::-1])
        i=0
        while i <len(l):
            if l[i]=='I':
                r+=1
            elif l[i]=='V':
                if i<len(l)-1 and l[i+1]=='I':
                    r+=4
                    i+=1
                else:
                    r+=5
            elif l[i]=='X':
                if i<len(l)-1 and l[i+1]=='I':
                    r+=9
                    i+=1
                else:
                    r+=10
            elif l[i]=='L':
                if i<len(l)-1 and l[i+1]=='X':
                    r+=40
                    i+=1
                else:
                    r+=50
            elif l[i]=='C':
                if i<len(l)-1 and l[i+1]=='X':
                    r+=90
                    i+=1
                else:
                    r+=100
            elif l[i]=='D':
                if i<len(l)-1 and l[i+1]=='C':
                    r+=400
                    i+=1
                else:
                    r+=500
            elif l[i]=='M':
                if i<len(l)-1 and l[i+1]=='C':
                    r+=900
                    i+=1
                else:
                    r+=1000
            i+=1
        return r
