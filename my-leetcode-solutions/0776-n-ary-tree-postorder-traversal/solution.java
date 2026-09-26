class Solution {
    public List<Integer> postorder(Node root) {
        List<Integer> list = new ArrayList<>();
        traverse(root, list);
        return list;
    }
    
    private void traverse(Node node, List<Integer> list) {
        if (node == null) {
            return;
        }
        for (Node child : node.children) {
            traverse(child, list);
        }
        list.add(node.val);
    }
}
