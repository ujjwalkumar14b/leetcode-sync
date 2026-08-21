import math

class Solution:
    def numSquares(self, n: int) -> int:
        # Helper to check if a number is a perfect square
        def is_square(x: int) -> bool:
            sq = int(math.sqrt(x))
            return sq * sq == x

        # Case 1: The number itself is a perfect square
        if is_square(n):
            return 1

        # Case 4: Legendre's Theorem check for 4^a * (8b + 7)
        temp = n
        while temp % 4 == 0:
            temp //= 4
        if temp % 8 == 7:
            return 4

        # Case 2: Check if it can be split into two perfect squares
        max_square = int(math.sqrt(n)) + 1
        for i in range(1, max_square):
            if is_square(n - i * i):
                return 2

        # Case 3: If it's not 1, 2, or 4, it must be 3
        return 3

