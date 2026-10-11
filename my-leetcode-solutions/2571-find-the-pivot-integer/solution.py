class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        x = int(total_sum ** 0.5)
        
        if x * x == total_sum:
            return x
            
        return -1
        
