class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        freq = {}
        n = len(grid)
        total_numbers = n * n        
        expected_sum = total_numbers * (total_numbers + 1) // 2
        actual_sum = 0            
        
        for row in grid:
            for num in row:
                actual_sum += num
                freq[num] = freq.get(num, 0) + 1
                if freq[num] == 2:
                    repeat = num
        
        missing = expected_sum - actual_sum + repeat
            
        return [repeat, missing]
        
