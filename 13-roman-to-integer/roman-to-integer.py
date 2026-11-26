class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        output= 0
        i = 0
        while i < len(s):
            if i < len(s)-1 and roman_int_dict[s[i+1]] >  roman_int_dict[s[i]]:
                output = output + (roman_int_dict[s[i+1]] - roman_int_dict[s[i]])
                i+=2
            else:
                output = output +roman_int_dict[s[i]]
                i+=1
        return output        