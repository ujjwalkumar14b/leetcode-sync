class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()

        moves = 0

        for i in range(len(seats)):
            moves += abs(seats[i] - students[i])

        return moves
