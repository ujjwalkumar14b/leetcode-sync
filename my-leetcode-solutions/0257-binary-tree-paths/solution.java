import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        if (root != null) {
            searchTree(root, "", result);
        }
        return result;
    }
    
    private void searchTree(TreeNode node, String path, List<String> result) {
        if (path.isEmpty()) {
            path = path + node.val;
        } else {
            path = path + "->" + node.val;
        }
        
        if (node.left == null && node.right == null) {
            result.add(path);
            return;
        }        
        if (node.left != null) {
            searchTree(node.left, path, result);
        }
        if (node.right != null) {
            searchTree(node.right, path, result);
        }
    }
}

