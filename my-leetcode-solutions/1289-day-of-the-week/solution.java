import java.time.LocalDate;

class Solution {
    public String dayOfTheWeek(int day, int month, int year) {

        String dayOfWeek = LocalDate.of(year, month, day).getDayOfWeek().name();
        return dayOfWeek.substring(0, 1) + dayOfWeek.substring(1).toLowerCase();
    }
}

