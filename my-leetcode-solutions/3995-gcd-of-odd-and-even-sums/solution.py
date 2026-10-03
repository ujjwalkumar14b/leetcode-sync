from math import gcd

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = 0
        even_sum = 0
        length = n * 2

        for i in range(1, length + 1):
            if i % 2 == 0:
                even_sum += i
            else:
                odd_sum += i

        return gcd(odd_sum, even_sum)
