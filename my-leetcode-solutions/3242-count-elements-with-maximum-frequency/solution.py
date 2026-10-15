from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:

        freq = Counter(nums)        
        max_f = max(freq.values())        
        total_frequencies = sum(f for f in freq.values() if f == max_f)
        
        return total_frequencies
