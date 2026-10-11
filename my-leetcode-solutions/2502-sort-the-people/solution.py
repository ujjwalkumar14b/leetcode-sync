class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        
        people = sorted(zip(heights, names), reverse=True)
        return [name for height, name in people]
