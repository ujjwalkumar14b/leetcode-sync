from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) <= 1:
            return [strs]

        anagrams = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())

