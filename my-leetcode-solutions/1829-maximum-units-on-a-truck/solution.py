class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:

        total_units = 0
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        for num_boxes, units_per_box in boxTypes:
            boxes_to_take = min(truckSize, num_boxes)
            total_units += boxes_to_take * units_per_box
            truckSize -= boxes_to_take
            
            if truckSize == 0:
                break
                
        return total_units
