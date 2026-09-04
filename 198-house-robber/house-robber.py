class Solution:
    def __init__(self):
        self.max_money_robed={}
    def max_robed(self,nums, house):
        if house == 0 :
            return nums[0]

        if house == 1:
            return max(nums[0], nums[1])

        if house in self.max_money_robed:
            return self.max_money_robed[house]

        last_house = self.max_robed(nums, house-2) + nums[house]
        last_of_last = self.max_robed(nums, house-1)

        self.max_money_robed[house] = max(last_house, last_of_last)

        return self.max_money_robed[house]

    def rob(self, nums: List[int]) -> int:
        house = len(nums)-1
        return self.max_robed(nums, house)
        