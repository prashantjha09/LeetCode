class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sub_array_sum = sum(nums[:k])
        max_sum = sub_array_sum
        i = 1
        j = k
        while i <=  j and j < len(nums):
            sub_array_sum = sub_array_sum - nums[i-1] + nums[j]
            max_sum = max(max_sum, sub_array_sum)
            i+=1
            j+=1
        return max_sum/k
        