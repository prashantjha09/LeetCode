from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count frequencies and sort characters by frequency in descending order
        frequency = dict(sorted(Counter(s).items(), key=lambda x: x[1], reverse=True))

        # Check if the reorganization is possible
        if any(count > (len(s) + 1) // 2 for count in frequency.values()):
            return ""

        # Initialize an output list with the length of s
        output_list = [None] * len(s)

        # Fill the list
        index = 0
        for char, count in frequency.items():
            for _ in range(count):
                # Place the character in the next available index
                output_list[index] = char
                index += 2
                # If we reach the end of the list, start filling odd indices
                if index >= len(s):
                    index = 1

        return "".join(output_list)