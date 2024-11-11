class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        answer_list = []
        min_element = min(nums)
        max_element = (max(nums))
        element_count = [0] * (max_element-min_element + 1)

        for i in range(len(nums)):
            if min_element >= 0:
                element_count[nums[i] - min_element] = element_count[nums[i] - min_element] + 1
            else:
                element_count[nums[i] + abs(min_element)] = element_count[nums[i] + abs(min_element)] + 1

        for i in range(len(element_count)):
            answer_list.extend([i + min_element] * element_count[i])
        return answer_list