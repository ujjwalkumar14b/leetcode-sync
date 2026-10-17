class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        arr = []
        
        for i in range(n):
            temp = nums[i]
            d_sum = 0
            while temp > 0:
                d_sum += temp % 10
                temp //= 10
            arr.append((d_sum, nums[i], i))
            
        arr.sort()        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue
                
            cycle_size = 0
            j = i
            
            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1
                
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps
