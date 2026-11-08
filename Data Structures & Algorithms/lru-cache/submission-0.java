class Node {
    int key;
    int value;
    Node next;
    Node prev;


    public Node(int key,int value) {
        this.key = key;
        this.value = value;
    }
}

class LRUCache {
    int capacity;
    Node head;
    Node tail;

    HashMap<Integer, Node> cache = new HashMap<>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head = new Node(0,0);
        tail = new Node(0,0);

        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if (cache.get(key) == null) {
            return -1;
        }

        removeNode(cache.get(key));
        addToHead(cache.get(key));

        return cache.get(key).value;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
        Node node = cache.get(key);
        node.value = value;

        removeNode(node);
        addToHead(node);
        return;
    }

        if (cache.size() >= capacity) {
            Node lru = tail.prev;
            cache.remove(lru.key);
            removeNode(lru);
    }
    
        Node n = new Node(key, value);
        addToHead(n);
        cache.put(key, n);
    }

    public void addToHead(Node node) {
        node.next = head.next;
        node.prev = head;

        head.next.prev = node;
        head.next = node;
    }

    public void removeNode(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
}
