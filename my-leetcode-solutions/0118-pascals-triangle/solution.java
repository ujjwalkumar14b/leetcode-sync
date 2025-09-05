import java.util.*;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();        
        result.add(new ArrayList<>());
        result.get(0).add(1);

        for (int i = 1; i < numRows; i++) {
            List<Integer> prevRow = result.get(i - 1);
            List<Integer> newRow = new ArrayList<>();
            
            newRow.add(1);
            for (int j = 1; j < i; j++) {
                newRow.add(prevRow.get(j - 1) + prevRow.get(j));
            }
            newRow.add(1);
            result.add(newRow);
        }
        return result;
    }
}

