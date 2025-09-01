class Solution {
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd;
        int childCount = 0; // keep track of how many children
    }

    private TrieNode root = new TrieNode();

    private void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) {
                node.children[idx] = new TrieNode();
                node.childCount++;
            }
            node = node.children[idx];
        }
        node.isEnd = true;
    }

    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        // Step 1: Build Trie
        for (String word : strs) {
            insert(word);
        }

        // Step 2: Find longest common prefix
        StringBuilder prefix = new StringBuilder();
        TrieNode node = root;

        while (node != null) {
            // stop if more than one branch OR a word ends
            if (node.childCount != 1 || node.isEnd) break;

            // find the single child
            for (int i = 0; i < 26; i++) {
                if (node.children[i] != null) {
                    prefix.append((char) ('a' + i));
                    node = node.children[i];
                    break;
                }
            }
        }

        return prefix.toString();
    }
}

