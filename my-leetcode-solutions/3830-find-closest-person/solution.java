class Solution {
    public int findClosest(int x, int y, int z) {
        int distanceX = Math.abs(z - x);
        int distanceY = Math.abs(z - y);
        
        if (distanceX < distanceY) {        // x is closer
            return 1; 
        } else if (distanceY < distanceX) { // y is closer
            return 2; 
        } else {
            return 0;                       // Both are equally close
        }
    }
}
