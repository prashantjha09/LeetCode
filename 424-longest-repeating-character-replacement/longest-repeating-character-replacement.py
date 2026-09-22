class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def get_max_char(char_count):
            max_count = sorted(char_count.values())[-1]
            return max_count
        char_count =  defaultdict(int)
        i = 0
        j = 0
        char_count[s[0]]+=1
        output = 1
        while i <= j and j < len(s)-1:
            j += 1
            char_count[s[j]] += 1
            max_char = get_max_char(char_count)
            if (j-i+1) - max_char <= k:
                tmp_max_length =  j-i+1
                output = max(tmp_max_length, output)
            else:
                char_count[s[i]] -= 1
                i+=1
        return output        