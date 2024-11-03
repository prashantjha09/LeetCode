class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        frequency = defaultdict(int)
        output = set()
        i = 0
        j = 1
        count = 0
        subarray = ""
        while i < j < len(s):
            if i == 0 and j == 1:
                subarray = s[i]+s[j]
                count += 2
                j += 1
                continue
            subarray += s[j]
            count += 1
            if count == 10:
                frequency[subarray] += 1
                if frequency[subarray] > 1:
                    output.add(subarray)
                subarray = subarray[1:]
                count -= 1
                i += 1
            j += 1
        return list(output)