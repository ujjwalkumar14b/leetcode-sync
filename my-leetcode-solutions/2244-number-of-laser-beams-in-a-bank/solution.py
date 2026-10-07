class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:

        count = 0
        prev_devices = 0

        for row in bank:
            curr_devices = row.count("1")

            if curr_devices > 0:
                count += prev_devices * curr_devices
                prev_devices = curr_devices

        return count
       
