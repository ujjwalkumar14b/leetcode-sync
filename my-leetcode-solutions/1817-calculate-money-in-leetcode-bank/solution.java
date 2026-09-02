class Solution {
    public int totalMoney(int n) {
        int weeks = n / 7;
        int remainingDays = n % 7;
        int firstWeekSum = 28;
        int lastWeekSum = firstWeekSum + 7 * (weeks - 1);
        int completeWeeksTotal = weeks * (firstWeekSum + lastWeekSum) / 2;
        int startingMoney = weeks + 1;
        int remainingDaysTotal = 0;
        
        for (int i = 0; i < remainingDays; i++) {
            remainingDaysTotal += startingMoney + i;
        }
        return completeWeeksTotal + remainingDaysTotal;
    }
}

