class Solution(object):
    def findWords(self, words):
        r1="qwertyuiop"
        r2="asdfghjkl"
        r3="zxcvbnm"
        r1n,r2n,r3n=0,0,0
        ans=[]
        for i in words:
            for j in i.lower():
                if j in r1:
                    r1n+=1
                elif j in r2:
                    r2n+=1
                else:
                    r3n+=1
            if r1n==len(i) or r2n==len(i) or r3n==len(i):
                ans.append(i)
            r1n,r2n,r3n=0,0,0
        return ans
