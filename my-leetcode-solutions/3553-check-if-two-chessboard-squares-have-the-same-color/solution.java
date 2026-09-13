class Solution {
    public boolean checkTwoChessboards(String coordinate1, String coordinate2) {

        int col1 = coordinate1.charAt(0) - 'a';
        int col2 = coordinate2.charAt(0) - 'a';
        int row1 = coordinate1.charAt(1) - '1';
        int row2 = coordinate2.charAt(1) - '1';
        int color1 = (col1 + row1) % 2;
        int color2 = (col2 + row2) % 2;

        return color1 == color2;
    }
}
