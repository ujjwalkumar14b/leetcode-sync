class Solution:
    def isBalanced(self, num: str) -> bool:

        even_sum = sum(int(d) for d in num[0::2])
        odd_sum = sum(int(d) for d in num[1::2])
        return even_sum == odd_sum

        
