class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jewel_set = set(jewels)
        return sum(1 for stone in stones if stone in jewel_set)
