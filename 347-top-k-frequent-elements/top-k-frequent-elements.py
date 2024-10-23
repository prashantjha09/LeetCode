from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i] = dic.get(i, 0)+1
        sorted_keys = dict(sorted(dic.items(), key=lambda d: d[1], reverse=True))
        return list(sorted_keys.keys())[:k]


        