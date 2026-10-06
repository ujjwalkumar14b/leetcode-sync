class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:

        idx_map = {ch: i for i, ch in enumerate(s)}
        return sum(abs(i - idx_map[ch]) for i, ch in enumerate(t))
        
