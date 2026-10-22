class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq = {}
        max_lucky = -1

        for num in arr:
            freq[num] = freq.get(num, 0) + 1
            
        for num, count in freq.items():
            if num == count:
                max_lucky = max(max_lucky, num)
                
        return max_lucky
