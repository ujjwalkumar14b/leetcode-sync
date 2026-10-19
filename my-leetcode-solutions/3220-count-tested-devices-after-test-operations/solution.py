class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested_count = 0
        for battery in batteryPercentages:
            if battery - tested_count > 0:
                tested_count += 1
                
        return tested_count
        
