class Solution(object):
    def intToRoman(self, num):
        d={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        r=''
        l=[]
        digit=len(str(num))
        a=num
        for i in range (digit,0,-1):
            a=a-(a%(10**(i-1)))
            l.append(a)
            a=num%(10**(i-1))
        for i in l:
            if len(str(i))==4:
                n=i/1000
                r=r+(d[1000]*n)
            elif len(str(i))==3:
                n=i/100
                if n>3:
                    if n==4:
                        r=r+d[100]+d[500]
                    elif n==9:
                        r=r+d[100]+d[1000]
                    else:
                        r=r+d[500]+(d[100]*((i-500)/100))
                else:
                    r=r+(d[100]*(i/100))
            elif len(str(i))==2:
                n=i/10
                if n>3:
                    if n==4:
                        r=r+d[10]+d[50]
                    elif n==9:
                        r=r+d[10]+d[100]
                    else:
                        r=r+d[50]+(d[10]*((i-50)/10))
                else:
                    r=r+(d[10]*(i/10))
            else:
                n=i
                if n>3:
                    if n==4:
                        r=r+d[1]+d[5]
                    elif n==9:
                        r=r+d[1]+d[10]
                    else:
                        r=r+d[5]+(d[1]*(i-5))
                else:
                    r=r+(d[1]*i)
        return r        
        
        