class Solution {
    public boolean areNumbersAscending(String s) {
        int prevNumber = -1;
        
        // Split the sentence by space to process individual words
        for (String token : s.split(" ")) {
            if (Character.isDigit(token.charAt(0))) {
                int currNumber = Integer.parseInt(token);
                
                if (currNumber <= prevNumber) {
                    return false;
                }                
                prevNumber = currNumber;
            }
        }
        return true;
    }
}

