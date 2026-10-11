class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        pref_counts = {0: students.count(0), 1: students.count(1)}
        
        for sandwich in sandwiches:
            if pref_counts[sandwich] > 0:
                pref_counts[sandwich] -= 1
            else:
                break
                
        return pref_counts[0] + pref_counts[1]
