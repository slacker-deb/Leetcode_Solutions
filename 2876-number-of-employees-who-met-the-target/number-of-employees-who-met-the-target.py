class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        hours.sort()
        l,r,a=0,len(hours)-1,len(hours)
        while l<=r:
            m=(l+r)//2
            if hours[m]>=target:
                a=m
                r=m-1
            else:
                l=m+1
        return len(hours)-a

        