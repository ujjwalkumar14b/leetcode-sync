class Solution:
    def minimumChairs(self, s: str) -> int:
        current_chairs = 0
        max_chairs = 0
        
        for char in s:
            if char == 'E':
                current_chairs += 1
            else:
                current_chairs -= 1
                
            if current_chairs > max_chairs:
                max_chairs = current_chairs
                
        return max_chairs
