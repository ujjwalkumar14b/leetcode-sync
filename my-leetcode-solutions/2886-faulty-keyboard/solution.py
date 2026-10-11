class Solution:
    def finalString(self, s: str) -> str:
        current_screen = []
        
        for char in s:
            if char == 'i':
                current_screen.reverse()
            else:
                current_screen.append(char)
                
        return "".join(current_screen)
