class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for word in words:
            total_weight = sum(weights[ord(c) - ord('a')] for c in word)            
            rem = total_weight % 26            
            res.append(chr(ord('z') - rem))
            
        return "".join(res)
