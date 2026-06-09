class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal:
            return True
        if len(s)!=len(goal):
            return False
        for i in range(len(s)-1):
            c=s[i+1:]+s[0:i+1]
            if c==goal:
                return True
        return False

        