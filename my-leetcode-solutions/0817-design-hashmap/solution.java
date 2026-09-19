class MyHashMap {
    private static final int SIZE = 2069; // A prime number to reduce collisions
    private LinkedList<Entry>[] buckets;

    private static class Entry {
        int key;
        int value;

        Entry(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    public MyHashMap() {
        buckets = new LinkedList[SIZE];
        for (int i = 0; i < SIZE; i++) {
            buckets[i] = new LinkedList<>();
        }
    }
    
    public void put(int key, int value) {
        int index = getIndex(key);
        for (Entry entry : buckets[index]) {
            if (entry.key == key) {
                entry.value = value; // Update existing key
                return;
            }
        }
        buckets[index].add(new Entry(key, value)); // Insert new key-value pair
    }
    
    public int get(int key) {
        int index = getIndex(key);
        for (Entry entry : buckets[index]) {
            if (entry.key == key) {
                return entry.value;
            }
        }
        return -1; // Key not found
    }
    
    public void remove(int key) {
        int index = getIndex(key);
        Iterator<Entry> iterator = buckets[index].iterator();
        while (iterator.hasNext()) {
            Entry entry = iterator.next();
            if (entry.key == key) {
                iterator.remove();
                return;
            }
        }
    }

    private int getIndex(int key) {
        return Integer.hashCode(key) % SIZE;
    }
}


/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
