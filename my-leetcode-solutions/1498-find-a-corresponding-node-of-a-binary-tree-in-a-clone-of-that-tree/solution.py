class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if not original:
            return None
            
        if original is target:
            return cloned
            
        left_res = self.getTargetCopy(original.left, cloned.left, target)
        if left_res:
            return left_res
            
        return self.getTargetCopy(original.right, cloned.right, target)
