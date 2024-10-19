class Solution {
    public char findKthBit(int n, int k) {
        // Base case
        if (n == 1) {
            return '0'; 
        }
        int lengthPrev = (1 << n) - 1; 
        if (k <= lengthPrev / 2) {
            return findKthBit(n - 1, k); 
        } else if (k == (lengthPrev / 2) + 1) {
            return '1';
        } else {
            int newK = lengthPrev - k + 1; 
            char bit = findKthBit(n - 1, newK);
            return bit == '0' ? '1' : '0'; 
        }
    }
}

