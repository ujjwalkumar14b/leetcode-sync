class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        ans = []
        curr = 1
        
        for x in target:
            while curr < x:
                ans.extend(["Push", "Pop"])
                curr += 1
            
            ans.append("Push")
            curr += 1
            
        return ans
