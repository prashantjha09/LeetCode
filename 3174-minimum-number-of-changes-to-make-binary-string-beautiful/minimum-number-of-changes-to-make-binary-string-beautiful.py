class Solution:
    def minChanges(self, s: str) -> int:
        i = 0
        j = 1
        counter = 0
        while i < j <= len(s)-1:
            if s[i] != s[j]:
                counter += 1
            i += 2
            j = i+1
        return counter
