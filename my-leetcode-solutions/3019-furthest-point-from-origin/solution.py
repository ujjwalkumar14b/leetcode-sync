class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count_L = moves.count('L')
        count_R = moves.count('R')
        count_underscore = moves.count('_')
        
        if count_L >= count_R:
            return count_L + count_underscore - count_R
        else:
            return count_R + count_underscore - count_L
