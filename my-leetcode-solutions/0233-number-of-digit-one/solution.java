class Solution {
    public int countDigitOne(int n) {
        int count = 0;
        long position = 1; // start from ones place

        while (position <= n) {
            long higher = n / (position * 10);
            long current = (n / position) % 10;
            long lower = n % position;

            if (current == 0) {
                count += higher * position;
            } else if (current == 1) {
                count += higher * position + (lower + 1);
            } else {
                count += (higher + 1) * position;
            }

            position *= 10;
        }

        return count;
    }
}

