class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        val_set = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i!=j and j !=k and i!=k and digits[i] !=0:
                        val = digits[i]*100+digits[j]*10+digits[k]
                        if val%2==0:
                            val_set.add(val)
        return len(val_set)
