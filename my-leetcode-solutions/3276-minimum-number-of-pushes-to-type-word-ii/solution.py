from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)        
        sorted_frequencies = sorted(counts.values(), reverse=True)
        total_pushes = 0

        for i, freq in enumerate(sorted_frequencies):
            cost = (i // 8) + 1
            total_pushes += freq * cost
            
        return total_pushes
