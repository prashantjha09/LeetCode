class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        tmp_max_sum = nums[0]
        for i in range(1, len(nums)):

            if current_sum + nums[i] < nums[i]:
                current_sum = nums[i]
            else:
                current_sum = current_sum + nums[i]
            tmp_max_sum =max(current_sum,tmp_max_sum)
        return tmp_max_sum
        
        