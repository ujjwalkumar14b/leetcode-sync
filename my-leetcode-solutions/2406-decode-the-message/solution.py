class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        mapping = {' ': ' '}
        current_char = ord('a')
        
        for char in key:
            if char not in mapping:
                mapping[char] = chr(current_char)
                current_char += 1
                
        decoded_message = []
        for char in message:
            decoded_message.append(mapping[char])
            
        return "".join(decoded_message)
