class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.isEmpty()) return 0; // edge case

        int hLen = haystack.length();
        int nLen = needle.length();

        for (int i = 0; i <= hLen - nLen; i++) {
            if (haystack.substring(i, i + nLen).equals(needle)) {
                return i; // return the index of the first occurrence
            }
        }

        return -1; // not found
    }
}

