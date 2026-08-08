from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        counts = Counter(nums)        
        return [num for num, count in counts.items() if count == 1]
