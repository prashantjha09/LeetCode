class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority_criteria = (len(nums) // 3) + 1
        nums = sorted(nums)
        digit = float("inf")
        answer_list = []
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] != digit:
                digit = nums[i]
                count = 1
            elif nums[i] == digit:
                count += 1
            if count == majority_criteria:
                if answer_list :
                    if answer_list[-1] != digit:
                        answer_list.append(digit)
                else:
                    answer_list.append(digit)

            print(nums[i], digit, count)
            i += 1
        return answer_list

        