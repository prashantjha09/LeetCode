class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        i=0
        while True:
            if i*i == x:
                return i
            if i*i > x:
                return i-1
            i+=1