class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        a = 0
        while i < j:
            s = (j - i) * min(height[i], height[j])
            a = max(a, s) 
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1      
        return a
