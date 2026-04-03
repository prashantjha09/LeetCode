class Solution(object):
    def maxSubArray(self, nums):
        prefix_sum_list= [0]
        prefix_sum = 0
        for i in nums:
            prefix_sum=prefix_sum + i
            prefix_sum_list.append(prefix_sum)


        #Minimum element till the index
        min_num = float('inf')
        min_list = []
        for i in prefix_sum_list:
            min_num=min(i, min_num)
            min_list.append(min_num)


        max_subarray = - float('inf')
        for i in range(1, len(prefix_sum_list)):
            max_subarray =  max(max_subarray, prefix_sum_list[i]-min_list[i-1])

        return max_subarray

