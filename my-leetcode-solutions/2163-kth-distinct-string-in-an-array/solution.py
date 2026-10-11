from collections import Counter

class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        counts = Counter(arr)
        distinct_count = 0
        
        for s in arr:
            if counts[s] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return s
                    
        return ""
