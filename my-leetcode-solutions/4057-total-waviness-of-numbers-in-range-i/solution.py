class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        count = 0
        for num in range(num1, num2 + 1):
            s = str(num)
            for i in range(1, len(s) - 1):
                if s[i - 1] < s[i] > s[i + 1]: 
                    count += 1
                elif s[i - 1] > s[i] < s[i + 1]:
                    count += 1
            
        return count

