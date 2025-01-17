class Solution {
  public boolean doesValidArrayExist(int[] derived) {
    return Arrays.stream(derived).reduce((a, b) -> a ^ b).getAsInt() == 0;
  }
}
