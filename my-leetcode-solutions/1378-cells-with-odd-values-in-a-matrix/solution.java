class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        
        int[] rowCounts = new int[m];
        int[] colCounts = new int[n];
        int oddRows = 0;
        int oddCols = 0;
        
        for (int[] index : indices) {
            rowCounts[index[0]]++;
            colCounts[index[1]]++;
        }
        for (int r : rowCounts) {
            if (r % 2 != 0) {
                oddRows++;
            }
        }
        for (int c : colCounts) {
            if (c % 2 != 0) {
                oddCols++;
            }
        }
        
        int evenRows = m - oddRows;
        int evenCols = n - oddCols;
        
        return (oddRows * evenCols) + (evenRows * oddCols);
    }
}
