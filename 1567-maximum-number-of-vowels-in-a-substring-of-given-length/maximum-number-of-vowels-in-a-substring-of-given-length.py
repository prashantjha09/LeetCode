class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        vowels_in_subarray = 0
        print(s[:k])
        for i in s[:k] :
            if i in vowels:
                vowels_in_subarray+=1
        output = vowels_in_subarray
        i = 1
        j = i+k-1
        while i<=j and j< len(s):
            if s[i-1] in vowels:
             vowels_in_subarray = vowels_in_subarray -1
            if s[j]  in vowels :
                vowels_in_subarray = vowels_in_subarray + 1

            output = max(output,vowels_in_subarray)
            i+=1
            j+=1
        return  output          