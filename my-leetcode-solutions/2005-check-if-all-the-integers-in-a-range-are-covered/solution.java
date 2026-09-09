class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {

        int[] diff = new int[52]; 
        int coverage = 0;

        for (int[] range : ranges) {
            diff[range[0]]++;
            diff[range[1] + 1]--;
        }
        for (int i = 1; i <= 50; i++) {
            coverage += diff[i];
            if (i >= left && i <= right && coverage <= 0) {
                return false;
            }
        }
        return true;
    }
}

