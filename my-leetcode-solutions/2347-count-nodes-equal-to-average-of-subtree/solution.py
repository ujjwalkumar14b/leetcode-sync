class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.result = 0
        
        def post_order(node):
            if not node:
                return 0, 0  
            
            left_sum, left_count = post_order(node.left)
            right_sum, right_count = post_order(node.right)
            
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            if node.val == current_sum // current_count:
                self.result += 1
                
            return current_sum, current_count

        post_order(root)
        return self.result
