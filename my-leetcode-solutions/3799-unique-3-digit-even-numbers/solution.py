from collections import Counter

class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        digit_count = Counter(digits)
        valid_count = 0
        
        for num in range(100, 1000, 2):
            hundreds = num // 100
            tens = (num // 10) % 10
            units = num % 10
            
            num_freq = Counter([hundreds, tens, units])
            
            possible = True
            for d, freq in num_freq.items():
                if digit_count[d] < freq:
                    possible = False
                    break
                    
            if possible:
                valid_count += 1
                
        return valid_count
