class Solution:
    def countPoints(self, rings: str) -> int:
        rod_colors = {i: set() for i in range(10)}
        
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = int(rings[i + 1])
            rod_colors[rod].add(color)
            
        count = 0
        for rod in range(10):
            if len(rod_colors[rod]) == 3:
                count += 1
                
        return count
