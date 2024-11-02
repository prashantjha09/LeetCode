class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        final_count = 1
        square_exist = defaultdict(int)
        for i in nums:
            square_exist[i] = 1
        nums = sorted(nums)
        for i in nums:
            val = i
            count = 1
            while True:
                if square_exist[val]:
                    square_val = pow(val, 2)
                    if square_exist[square_val] == 1:
                        val = square_val
                        count += 1
                    else:
                        break
            final_count = max(count, final_count)
        return final_count if final_count > 1 else -1

        