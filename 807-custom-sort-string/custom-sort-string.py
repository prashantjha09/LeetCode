from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count =  defaultdict(int)
        output = ""
        for element in s:
            s_count[element]=s_count[element]+1
        for char in order:
            for count in range(s_count[char]):
                output = output + char
            del  s_count[char]
        for char in  s_count:
            for count in range(s_count[char]):
                output = output + char
        return output






        

        