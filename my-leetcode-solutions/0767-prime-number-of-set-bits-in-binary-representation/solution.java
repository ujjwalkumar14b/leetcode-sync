class Solution {
    public int countPrimeSetBits(int left, int right) {
        
        int primeMask = 665772;
        int primeSetBitCount = 0;
        
        for (int i = left; i <= right; i++) {
            int setBits = Integer.bitCount(i);
            if (((primeMask >> setBits) & 1) == 1) {
                primeSetBitCount++;
            }
        }
        return primeSetBitCount;
    }
}
