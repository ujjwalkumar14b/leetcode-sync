class Solution:
    def convertDateToBinary(self, date: str) -> str:

        parts = date.split('-')        
        binary_parts = []
        
        for part in parts:
            binary_parts.append(bin(int(part))[2:])
        
        return '-'.join(binary_parts)
        
