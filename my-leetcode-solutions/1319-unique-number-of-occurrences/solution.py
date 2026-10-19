class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        return len(set(freq.values())) == len(freq.values())
