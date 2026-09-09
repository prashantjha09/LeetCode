class Solution:

    def is_equal_sum_Partition(self, nums, index, target, memo):

        if target == 0:
            return True

        if index == len(nums) or target < 0:
            return False

        if (index, target) in memo:
            return memo[(index, target)]

        # Take nums[index]
        option_1 = self.is_equal_sum_Partition(
            nums, index + 1, target - nums[index], memo
        )

        # Don't take nums[index]
        option_2 = self.is_equal_sum_Partition(
            nums, index + 1, target, memo
        )

        memo[(index, target)] = option_1 or option_2

        return memo[(index, target)]

    def canPartition(self, nums: list[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        memo = {}

        return self.is_equal_sum_Partition(nums, 0, target, memo)