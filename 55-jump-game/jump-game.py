from collections import defaultdict
class Solution:
    def __init__(self):
        self.dp =  defaultdict(lambda: None)

    def jump(self, nums, index):
        if index == 0:
            return True
        if self.dp[index] is not None:
            return self.dp[index]
        for prior_index in range(index):
            element = nums[prior_index]
            if index - prior_index <= element:
                if self.jump(nums, prior_index)==True:
                    self.dp[index] = True
                    return True
        self.dp[index] =False
        return False

        self.dp[index] =False
        return False


    def canJump(self, nums: List[int]) -> bool:
        index = len(nums)-1
        return self.jump(nums, index)
        