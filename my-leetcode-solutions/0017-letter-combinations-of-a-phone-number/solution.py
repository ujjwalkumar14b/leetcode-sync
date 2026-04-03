class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, path):
            # If the combination is complete
            if index == len(digits):
                result.append(path)
                return
            
            # Get letters for current digit
            for char in phone[digits[index]]:
                backtrack(index + 1, path + char)
        
        backtrack(0, "")
        return result
