class Solution:
    def makeFancyString(self, s: str) -> str:
        final_s = ""  
        repeated_char = 0  

        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                repeated_char += 1
            else:
                repeated_char = 0  

            if repeated_char < 2:
                final_s += s[i]

        return final_s
