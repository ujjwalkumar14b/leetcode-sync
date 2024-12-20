class Solution {
    public boolean isPalindrome(int x) {
        int m = x;
        int sum = 0;
        if(x<0){
            return false;
        }
        while(m>0){
            int r = m%10;
            sum = sum*10 + r;
            m = m/10;
        }
        return sum == x;
    }
}
