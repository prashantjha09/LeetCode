class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        count = 0
        while j > i:
            element_sum = nums[j] + nums[i]
            if element_sum == k:
                count += 1
                i += 1
                j -= 1
            elif element_sum > k:
                j -= 1
            else:
                i += 1
        return count

        