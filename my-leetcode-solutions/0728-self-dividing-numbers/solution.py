class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        for num in range(left, right + 1):
            temp = num
            is_valid = True

            while temp > 0:
                digit = temp % 10
                if digit == 0 or num % digit != 0:
                    is_valid = False
                    break
                temp //= 10

            if is_valid:
                result.append(num)

        return result

