class Solution:
    def maxPower(self, s: str) -> int:
        tmp_len = 1
        max_len = 1
        for i in range(len(s)-1):
            if s[i] ==  s[i+1]:
                tmp_len += 1
            else:
                max_len = max(max_len, tmp_len)
                tmp_len = 1
        max_len = max(max_len, tmp_len)
        return max_len

