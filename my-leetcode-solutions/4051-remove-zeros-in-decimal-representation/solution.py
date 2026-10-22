class Solution:
    def removeZeros(self, n: int) -> int:
        str_n = str(n)
        result_chars = []
        
        for digit in str_n:
            if digit != "0":
                result_chars.append(digit)

        return int("".join(result_chars))
