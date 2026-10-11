class Solution:
    def countAsterisks(self, s: str) -> int:
        is_inside_pair = False
        count = 0
        
        for char in s:
            if char == '|':
                is_inside_pair = not is_inside_pair
            elif char == '*' and not is_inside_pair:
                count += 1
                
        return count
