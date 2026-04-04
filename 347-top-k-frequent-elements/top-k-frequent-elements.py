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
        cnt = 0
        for i in reversed(counter):
            for j in counter[i] :
                output.append(j)
                cnt+=1
                if k-cnt==0:
                    return output

