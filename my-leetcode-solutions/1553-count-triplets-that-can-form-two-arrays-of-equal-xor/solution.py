class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        n = len(arr)
        count = 0
        
        for i in range(n):
            current_xor = 0
            for k in range(i, n):
                current_xor ^= arr[k]
                if current_xor == 0 and k > i:
                    count += (k - i)
                    
        return count
        
