class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        
        start_cities = {path[0] for path in paths}
        
        for path in paths:
            destination = path[1]
            if destination not in start_cities:
                return destination
                
        return ""
