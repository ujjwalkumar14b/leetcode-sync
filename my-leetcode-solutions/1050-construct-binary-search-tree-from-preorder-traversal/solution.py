class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)
        current = root
        
        for val in preorder[1:]:
            node = TreeNode(val)
            if val < stack[-1].val:
                stack[-1].left = node
                stack.append(node)
            else:
                last_popped = None
                while stack and stack[-1].val < val:
                    last_popped = stack.pop()
                last_popped.right = node
                stack.append(node)
                
        return root
