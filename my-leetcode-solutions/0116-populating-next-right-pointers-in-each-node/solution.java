class Solution {
    public Node connect(Node root) {
        if (root == null) return null;
        connectTwoNodes(root.left, root.right);
        return root;
    }

    private void connectTwoNodes(Node node1, Node node2) {
        if (node1 == null || node2 == null) return;

        // Connect two adjacent nodes
        node1.next = node2;

        // Connect children of the same parent
        connectTwoNodes(node1.left, node1.right);
        connectTwoNodes(node2.left, node2.right);

        // Connect across parents
        connectTwoNodes(node1.right, node2.left);
    }
}

