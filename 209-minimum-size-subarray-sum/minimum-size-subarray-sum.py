class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum_list=[0]+list(accumulate(nums))

        i = 0
        j = 1
        min_subarray =  float("inf")
        while i < j < len(prefix_sum_list):
            if prefix_sum_list[j] -  prefix_sum_list[i] >= target:
                min_subarray = min(min_subarray, j-i)
                i+=1
            else:
                j+=1

        return min_subarray if min_subarray != float("inf") else 0