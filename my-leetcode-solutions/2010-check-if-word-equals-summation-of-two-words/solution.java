class Solution {
    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        return (getNumericalValue(firstWord) + getNumericalValue(secondWord)) == getNumericalValue(targetWord);
    }

    private int getNumericalValue(String word) {
        int value = 0;
        for (int i = 0; i < word.length(); i++) {
            value = value * 10 + (word.charAt(i) - 'a');
        }
        return value;
    }
}

