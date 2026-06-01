class Solution(object):
    def defangIPaddr(self, address):
        r=address.replace('.','[.]')
        return r
        