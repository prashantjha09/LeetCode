class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left  = 0
        right = len(nums)-1
        while left<=right:
            if len(nums[left:right]) <= 2:
                return nums.index(max(nums))            
            mid = (left + right) // 2
            if mid == 0 and nums[mid] > nums[mid+1]:
                return mid
            if mid == len(nums)-1 and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] > nums[mid]:
                right = mid-1
            else:
                left = mid+1
        