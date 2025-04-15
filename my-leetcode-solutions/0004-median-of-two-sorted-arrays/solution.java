import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        ArrayList<Integer> list = new ArrayList<>();

        // Add elements from nums1
        for (int i = 0; i < nums1.length; i++) {
            list.add(nums1[i]);
        }

        // Add elements from nums2
        for (int i = 0; i < nums2.length; i++) {
            list.add(nums2[i]);
        }

        // Sort the combined list
        Collections.sort(list);

        int size = list.size();

        if (size % 2 != 0) {
            // Odd number of elements
            return list.get(size / 2);
        } else {
            // Even number of elements
            return (list.get(size / 2 - 1) + list.get(size / 2)) / 2.0;
        }
    }
}

