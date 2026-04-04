class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums = [1]+ nums + [1]
        prefix_multiply_list = []
        prefix_multi = 1
        for index in range(1,len(nums)-1):
            prefix_multi = prefix_multi*nums[index -1]
            prefix_multiply_list.append(prefix_multi)

        sufix_multiply_list = []
        sufix_multi = 1
        for index in reversed(range(1, len(nums) - 1)):
            sufix_multi = sufix_multi * nums[index + 1]
            sufix_multiply_list.append(sufix_multi)

        return [i*j for i,j in zip(reversed(sufix_multiply_list),prefix_multiply_list)]



        