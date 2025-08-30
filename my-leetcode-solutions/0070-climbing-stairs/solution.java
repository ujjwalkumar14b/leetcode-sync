class Solution {
    public int climbStairs(int n) {
        int f[] = new int[n+1];
        return climbStairsHelper(n, f);
    }
    public int climbStairsHelper(int n, int f[]) {
        if(n == 1 || n == 2){
            return n;
        }
        if(f[n] != 0){
            return f[n];
        }
        f[n] =  climbStairsHelper(n-1, f) + climbStairsHelper(n-2, f);
        return f[n];
    }
}
