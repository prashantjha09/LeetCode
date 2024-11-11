class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prime_index = [0] * 1001

        def check_strictly_less_prime(element):
            j = element - 1
            if prime_index[j] == 2:
                return j
            while prime_index[j] == 0 or j > 1:
                if prime_index[j] == 1:
                    return j
                j -= 1
            return j

        def is_prime(check_num):
            if check_num <= 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if check_num % i == 0:
                    return False
            return True

        for n in range(1, 1001):
            if is_prime(n):
                prime_index[n] = 1

        last_number = -1
        for i in nums:
            if i <= 2:
                if i > last_number:
                    last_number = i
                else:
                    return False
            else:
                check_prime_for = i
                while True:
                    tmp_i = i
                    prime = check_strictly_less_prime(check_prime_for)
                    val = tmp_i - prime
                    if val > last_number:
                        last_number = val
                        break
                    else:
                        if prime == 2:
                            if tmp_i > last_number:
                                last_number = tmp_i
                                break
                            else:
                                return False
                        check_prime_for = prime
        return True