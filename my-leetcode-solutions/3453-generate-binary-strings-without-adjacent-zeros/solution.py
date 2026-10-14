class Solution:
    def validStrings(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_string):
            # If the string reaches length n, add it to our results
            if len(current_string) == n:
                result.append(current_string)
                return
            
            backtrack(current_string + '1')
            
            if not current_string or current_string[-1] != '0':
                backtrack(current_string + '0')
                
        backtrack("")
        return result
