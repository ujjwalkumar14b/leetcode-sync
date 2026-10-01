class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str: 
        return ''.join(char for idx, char in sorted(zip(indices, s)))
