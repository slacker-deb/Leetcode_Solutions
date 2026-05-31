class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        check = strs[0]
        for j in range(1, len(strs)):
            burger = ""

            for i in range(min(len(check), len(strs[j]))):
                if check[i] == strs[j][i]:
                    burger += check[i]
                else:
                    break
            check = burger
        return check