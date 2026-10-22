class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:

        order_map = {val: i for i, val in enumerate(arr2)}
        return sorted(
            arr1, key=lambda x: (0, order_map[x]) if x in order_map else (1, x)
        )
        
