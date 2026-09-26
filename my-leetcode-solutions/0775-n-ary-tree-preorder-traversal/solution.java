class Solution {
    public List<Integer> preorder(Node root) {
        List<Integer> list = new ArrayList<>();
        traverse(root, list);
        return list;
    }
    
    private void traverse(Node node, List<Integer> list) {
        if (node == null) {
            return;
        }
        list.add(node.val);
        for (Node child : node.children) {
            traverse(child, list);
        }
    }
}
