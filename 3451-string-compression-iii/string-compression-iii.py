class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        j = 1
        tmp_com = 1
        while i < j < len(word):
            if word[i] == word[j]:
                if tmp_com == 9:
                    comp += f"{tmp_com}{word[i]}"
                    i = j
                    j += 1
                    tmp_com = 1
                else:
                    j += 1
                    tmp_com += 1
            elif tmp_com == 9:
                comp += f"{tmp_com}{word[i]}"
                i = j
                j += 1
                tmp_com = 1
            else:
                comp += f"{tmp_com}{word[i]}"
                tmp_com = 1
                i = j
                j += 1
        comp += f"{tmp_com}{word[i]}"
        return comp        