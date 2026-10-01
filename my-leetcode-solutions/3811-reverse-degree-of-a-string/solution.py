class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s, 1):
            char_val = ord('z') - ord(char) + 1
            total += char_val * i
        return total
