class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_set = set(friends)
        return [id_val for id_val in order if id_val in friends_set]
