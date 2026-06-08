class LRUCache {
public:
    struct Node{
        int key;
        int val;
        Node* prev;
        Node* next;

        Node(int k, int v){
            key = k;
            val = v;
            prev = nullptr;
            next = nullptr;
        }
    };

private:
    int cap;
    unordered_map<int,Node*> cache;
    Node* head;
    Node* tail;

    void add(Node* node){
        node->next = head->next;
        node->prev = head;
        head->next->prev = node;
        head->next = node;
    }

    void remove(Node* node){
        node->prev->next = node->next;
        node->next->prev = node->prev;
        node->next = nullptr;
        node->prev = nullptr;
    }

public:
    LRUCache(int capacity) {
        cap = capacity;
        head = new Node(-1,-1);
        tail = new Node(-1,-1);

        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if(cache.find(key) == cache.end()) return -1;
        Node* node = cache[key];
        remove(node);
        add(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if(cache.find(key) != cache.end()){
            Node* node = cache[key];
            node->val = value;
            remove(node);
            add(node);
            return;
        }
        if(cache.size()==cap){
            Node* lastNode = tail->prev;
            cache.erase(lastNode->key);
            remove(tail->prev);
            delete lastNode;
        }
        Node* newNode = new Node(key,value);
        cache[key] = newNode;
        add(newNode);

    }
};
