class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total = 0
        n = len(arr)

        for i in range(n):
            current = 0
            for j in range(i, n):
                current += arr[j]
                if (j - i + 1) % 2 == 1:
                    total += current

        return total
        
