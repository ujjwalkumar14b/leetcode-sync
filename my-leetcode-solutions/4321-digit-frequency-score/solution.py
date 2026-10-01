class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum(int(digit) for digit in str(abs(n)))
