class Solution {
    public int arrangeCoins(int n) {
        long left = 1, right = n;
        long res = 0;
        
        while (left <= right) {
            long mid = left + (right - left) / 2;
            long coinsNeeded = mid * (mid + 1) / 2;
            
            if (coinsNeeded <= n) {
                res = mid;
                left = mid + 1; 
            } else {
                right = mid - 1; 
            }
        }
        return (int) res;
    }
}
