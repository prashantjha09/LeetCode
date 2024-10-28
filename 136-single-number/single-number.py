class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for i in nums:
            answer = answer^i
        return answer   


        
        