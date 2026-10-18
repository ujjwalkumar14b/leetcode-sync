class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        freq_target = {}
        freq_arr = {}

        for num in target:
            freq_target[num] = freq_target.get(num, 0) + 1

        for num in arr:
            freq_arr[num] = freq_arr.get(num, 0) + 1


        return freq_target == freq_arr

