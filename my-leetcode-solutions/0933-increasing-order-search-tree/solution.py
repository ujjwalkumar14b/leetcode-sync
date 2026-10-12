class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        nodes = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
            
        inorder(root)
        
        new_root = nodes[0]
        curr = new_root
        curr.left = None
        
        for i in range(1, len(nodes)):
            next_node = nodes[i]
            next_node.left = None
            curr.right = next_node
            curr = next_node
            
        curr.right = None
        return new_root
