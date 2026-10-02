class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag1 = set()  # (r - c)
        diag2 = set()  # (r + c)
        
        def backtrack(row: int) -> int:
            if row == n:
                return 1
            
            solutions = 0
            for col in range(n):
                d1 = row - col
                d2 = row + col
                
                if col in cols or d1 in diag1 or d2 in diag2:
                    continue
                    
                cols.add(col)
                diag1.add(d1)
                diag2.add(d2)
                
                solutions += backtrack(row + 1)
                
                cols.remove(col)
                diag1.remove(d1)
                diag2.remove(d2)
                
            return solutions

        return backtrack(0)
