public class Solution extends GuessGame {
  public int guessNumber(int n) {
    int left = 1;
    int right = n;

    while (left < right) {
      final int mid = left + (right - left) / 2;
      if (guess(mid) <= 0) 
        right = mid;
      else
        left = mid + 1;
    }
    return left;
  }
}
