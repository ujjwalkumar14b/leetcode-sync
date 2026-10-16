class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLength = []
        count = 0

        for rectangle in rectangles:
            maxLength.append(min(rectangle[0], rectangle[1]))

        for length in maxLength:
            if length == max(maxLength):
                count += 1

        return count

