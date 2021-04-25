class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cha=ord(s[0])-ord(t[0])

        for i in range(len(s)):
            if ord(s[i]) - ord(t[i]) == cha:
                continue
            else:
                return False
            
p=Solution()
print(p.isIsomorphic('add','egg'))