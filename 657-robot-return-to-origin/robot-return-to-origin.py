class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = {"U":0, "D":0, "L":0, "R":0}
        for i in moves:
            counter[i]=counter[i]+1
        return True if counter["U"]==counter["D"] and counter["L"]==counter["R"] else False


        