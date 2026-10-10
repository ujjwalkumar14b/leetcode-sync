class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        
        result = []
        
        for xj, yj, rj in queries:
            count = 0
            rj_sq = rj ** 2
            
            for x, y in points:
                if (x - xj) ** 2 + (y - yj) ** 2 <= rj_sq:
                    count += 1
                    
            result.append(count)
            
        return result
