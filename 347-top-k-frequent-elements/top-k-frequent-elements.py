class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        element_count = {i:0 for i in nums}
        for i in nums:
            element_count[i] = element_count[i]+1

        total_var = len(nums)
        counter = {i+1: [] for i in range(0,total_var)}
        for i in element_count:
            counter[element_count[i]].append(i)

        output = []
        for i in reversed(list(counter.keys())):
            occurrence_len = len(counter[i])
            if occurrence_len > 0:
                for val in counter[i]:
                    output.append(val)
                    k -= 1
                    if k == 0:
                        return output
