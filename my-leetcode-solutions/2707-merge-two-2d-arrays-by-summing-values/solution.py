class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        res = []
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        
        while i < n and j < m:
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            
            if id1 < id2:
                res.append([id1, val1])
                i += 1
            elif id2 < id1:
                res.append([id2, val2])
                j += 1
            else:
                res.append([id1, val1 + val2])
                i += 1
                j += 1
                
        while i < n:
            res.append(nums1[i])
            i += 1
            
        while j < m:
            res.append(nums2[j])
            j += 1
            
        return res
