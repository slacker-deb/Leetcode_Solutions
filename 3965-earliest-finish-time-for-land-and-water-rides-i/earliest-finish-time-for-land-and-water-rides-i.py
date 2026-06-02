class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        def ride(first, firsttime, second, secondtime):
            k=[]
            for i in range(len(first)):
                for j in range (len(second)):
                    if first[i]+firsttime[i]>second[j]:
                        c=first[i]+firsttime[i]+secondtime[j]
                    else:
                        c=second[j]+secondtime[j]
                    k.append(c)
            return k     
        l1=ride(landStartTime, landDuration, waterStartTime, waterDuration)
        l2=ride(waterStartTime, waterDuration, landStartTime, landDuration)
        l=l1+l2
        return min(l)