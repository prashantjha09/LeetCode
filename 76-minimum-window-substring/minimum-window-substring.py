class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        output_string = ""
        tmp_string = ""
        for i in t:
            if not t_count.get(i):
                t_count[i]=1
            else:
                t_count[i] += 1
        count = len(t_count)
        i =0
        j = 0
        while i<=j:
            if count == 0:
                if s[i] in t_count:
                    t_count[s[i]] += 1
                    if t_count[s[i]] > 0:
                        count = count + 1
                tmp_string = s[i:j]
                if not output_string or len(tmp_string) < len(output_string):
                    output_string = tmp_string
                i=i+1
            else:
                if j==len(s):
                    break
                if s[j] in t_count:
                    t_count[s[j]] -= 1
                    if t_count[s[j]] == 0:
                        count = count - 1
                tmp_string = tmp_string + s[j]
                j += 1
        return output_string