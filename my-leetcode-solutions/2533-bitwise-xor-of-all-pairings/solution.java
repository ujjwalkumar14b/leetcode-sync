class Solution {
  public int xorAllNums(int[] nums1, int[] nums2) {
    final int xors1 = Arrays.stream(nums1).reduce((a, b) -> a ^ b).getAsInt();
    final int xors2 = Arrays.stream(nums2).reduce((a, b) -> a ^ b).getAsInt();
    return (nums1.length % 2 * xors2) ^ (nums2.length % 2 * xors1);
  }
}
