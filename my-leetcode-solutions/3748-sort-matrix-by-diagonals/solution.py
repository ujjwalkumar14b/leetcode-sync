from collections import defaultdict

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = defaultdict(list)
        
        # Step 1: Collect elements by diagonal (r - c)
        for r in range(n):
            for c in range(n):
                diagonals[r - c].append(grid[r][c])
                
        # Step 2: Sort diagonals based on position
        for key in diagonals:
            if key >= 0:
                # Bottom-left triangle including main diagonal: descending
                diagonals[key].sort(reverse=True)
            else:
                # Top-right triangle: ascending
                diagonals[key].sort()
                
        # Step 3: Put elements back into the grid
        for r in range(n):
            for c in range(n):
                grid[r][c] = diagonals[r - c].pop(0)
                
        return grid
