class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        if len(nums)==1:
            return [pow(nums[0], 2)]
        left = 0
        right = len(nums)-1
        output = []
        while left <= right:
            if pow(nums[right], 2) >  pow(nums[left], 2):
                output.insert(0, pow(nums[right], 2))
                right-=1
            else:
                output.insert(0, pow(nums[left], 2))
                left +=1
        return output        