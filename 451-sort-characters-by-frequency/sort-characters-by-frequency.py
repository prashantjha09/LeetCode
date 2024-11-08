class Solution:
    def frequencySort(self, s: str) -> str:
        answer = ""
        frequency_hash = Counter(s)
        sorted_frequency_hash = sorted(frequency_hash.items(), key=lambda x: x[1], reverse=True)
        print(sorted_frequency_hash)
        for i in sorted_frequency_hash:
            answer += i[0] * i[1]
        return answer        
        