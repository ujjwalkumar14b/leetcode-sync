class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
            
        return [num for num, count in freq.items() if count == 2]
        
