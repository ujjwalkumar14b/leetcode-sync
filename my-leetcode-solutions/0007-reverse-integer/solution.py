class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        num = abs(x)
        reverse = 0

        while num > 0:
            rem = num % 10
            reverse = reverse * 10 + rem
            num = num // 10

        reverse *= sign

        # Check 32-bit signed integer range
        if reverse < -(2**31) or reverse > 2**31 - 1:
            return 0

        return reverse
