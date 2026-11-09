class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        int[] results = new int[k];
        
        for (int i = 0; i < k; i++) {
            int key = -1;
            int maxValue = -1;

            for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
                if (entry.getValue() > maxValue) {
                    maxValue = entry.getValue();
                    key = entry.getKey();
                }
            }
            results[i] = key;
            map.remove(key);
        }

        return results;
    }
}
