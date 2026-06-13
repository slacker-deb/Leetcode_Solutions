class Solution:
    def dayOfYear(self, date: str) -> int:
        def feb(x):
            if x%100==0:
                return 29 if x%400==0 else 28
            else:
                return 29
        l=date.split('-')
        m=[31,28,31,30,31,30,31,31,30,31,30,31]
        if int(l[0])%4==0:
            m[1]=feb(int(l[0]))
        return sum(m[0:int(l[1])-1])+int(l[2])
        
        