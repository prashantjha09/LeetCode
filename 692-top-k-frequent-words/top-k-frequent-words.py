class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = sorted(Counter(words).items(), key=lambda x: x[1], reverse=True)
        count_list = defaultdict(list)
        for i in frequency:
            count_list[i[1]].append(i[0])
        output = []
        for i in count_list:
            output.extend(sorted(count_list[i]))
            if len(output) >= k:
                return output[:k]
        return output[:k]