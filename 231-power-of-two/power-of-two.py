class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if  n < 2:
            return False
        else:
            n = n/2
            return self.isPowerOfTwo(n)
        