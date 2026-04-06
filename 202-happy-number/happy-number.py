class Solution:
    def check_if_happy(self, n, seen=None):
        if seen is None:
            seen = set()        
        n_list = [int(i) for i in str(n)]
        sum = 0
        for i in n_list:
            sum = sum + pow(i,2)
        if sum == 1:
            return True
        if n in seen:
            return False
        seen.add(n)
        return self.check_if_happy(sum, seen)        

    def isHappy(self, n: int) -> bool:
        return self.check_if_happy(n)
       
        