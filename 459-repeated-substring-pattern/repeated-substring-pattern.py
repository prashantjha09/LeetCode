class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)):
            count = s.count(s[0:i+1])
            if count*(i+1)== len(s) and count>1 :
                return True
        return False        