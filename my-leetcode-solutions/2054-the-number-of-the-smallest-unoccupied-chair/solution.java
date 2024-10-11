class Solution {
    public int smallestChair(int[][] times, int targetFriend) {
        List<int[]> events = new ArrayList<>();

        for (int i = 0; i < times.length; i++) {
            events.add(new int[]{times[i][0], 1, i}); 
            events.add(new int[]{times[i][1], -1, i});
        }

        Collections.sort(events, (a, b) -> {
            if (a[0] == b[0]) {
                return Integer.compare(a[1], b[1]); 
            }
            return Integer.compare(a[0], b[0]); 
        });

        PriorityQueue<Integer> availableChairs = new PriorityQueue<>();
        Map<Integer, Integer> occupiedChairs = new HashMap<>();

        // Process events
        for (int time[] : events) {
            int eventTime = time[0];
            int eventType = time[1]; 
            int friendIndex = time[2];

            if (eventType == -1) { 
                int chairNumber = occupiedChairs.remove(friendIndex);
                availableChairs.offer(chairNumber);
            } else { 
                int chairNumber;
                if (!availableChairs.isEmpty()) {
                    chairNumber = availableChairs.poll(); 
                } else {
                    chairNumber = occupiedChairs.size(); 
                }
                occupiedChairs.put(friendIndex, chairNumber);

                if (friendIndex == targetFriend) {
                    return chairNumber;
                }
            }
        }
        
        return -1; 
    }
}
