class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Sort digits of the given number n
        sorted_n = "".join(sorted(str(n)))

        # Check if sorted digits of n match any sorted digits of powers of 2
        powers_of_2 = ["".join(sorted(str(pow(2, val)))) for val in range(30)]
        if sorted_n in powers_of_2:
            return True
        else:
            return False

        