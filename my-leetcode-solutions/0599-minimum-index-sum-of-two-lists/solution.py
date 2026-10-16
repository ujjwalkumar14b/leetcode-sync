class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index_map = {word: i for i, word in enumerate(list1)}
        
        min_sum = float('inf')
        result = []
        
        for j, word in enumerate(list2):
            if word in index_map:
                current_sum = j + index_map[word]
                
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [word]
                elif current_sum == min_sum:
                    result.append(word)
                    
        return result
