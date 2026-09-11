class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dict = defaultdict(int)
        i = 0
        j = 1
        dict[nums[i]]+=1
        while i < j and j< len(nums):        
            dict[nums[j]]+=1
            if abs(i - j) > k :
                dict[nums[i]]-=1
                i += 1
            if dict[nums[j]] == 2:
                return True
            j+=1
        return False



