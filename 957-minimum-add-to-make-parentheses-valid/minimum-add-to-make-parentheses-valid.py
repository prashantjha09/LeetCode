class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        s_count = deque()
        for i in s:
            if not s_count :
                if i==')':
                    s_count.append(')')
                if i=='(':
                    s_count.append('(')
            else:
                if i==')':
                    if s_count[-1] == "(":
                        s_count.pop()
                    else:
                        s_count.append(')')
                if  i=='(':
                    s_count.append('(')
        return len(s_count)