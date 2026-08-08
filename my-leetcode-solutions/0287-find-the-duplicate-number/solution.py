from collections import Counter
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        return next(num for num, freq in count.items() if freq > 1)
