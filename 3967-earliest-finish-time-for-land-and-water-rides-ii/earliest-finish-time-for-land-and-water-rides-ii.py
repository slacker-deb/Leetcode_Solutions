class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        mn_land = min(landStartTime[i]+landDuration[i] for i in xrange(len(landStartTime)))
        mn_water = min(waterStartTime[i]+waterDuration[i] for i in xrange(len(waterStartTime)))
        return min(min(max(landStartTime[i], mn_water)+landDuration[i] for i in xrange(len(landStartTime))), min(max(waterStartTime[i], mn_land)+waterDuration[i] for i in xrange(len(waterStartTime))))