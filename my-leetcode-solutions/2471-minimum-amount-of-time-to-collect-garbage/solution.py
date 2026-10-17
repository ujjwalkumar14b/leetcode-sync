class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        total_time = sum(len(g) for g in garbage)
        last_seen = {}
        prefix_travel = [0] * len(garbage)

        for i, g in enumerate(garbage):
            for char in g:
                last_seen[char] = i
                
        for i in range(1, len(garbage)):
            prefix_travel[i] = prefix_travel[i-1] + travel[i-1]
            
        for char in "MPG":
            if char in last_seen:
                total_time += prefix_travel[last_seen[char]]
                
        return total_time
