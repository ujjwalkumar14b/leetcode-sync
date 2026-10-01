class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)
        answer = []
        
        for x in nums:
            right_sum -= x
            answer.append(abs(left_sum - right_sum))
            left_sum += x
            
        return answer
        
