class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(" ")
        if len(sentence) == 1:
            return sentence[0][0] == sentence[0][-1]
        else:
            for i in range(1, len(sentence)):
                if sentence[i][0] != sentence[i - 1][-1]:
                    return False
                if i == len(sentence) - 1:
                    if sentence[i][-1] != sentence[0][0]:
                        return False
            return True
