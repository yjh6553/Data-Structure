class DLL:
    def __init__(self, key, val):
        self.prev = None
        self.val = val
        self.key = key
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.MRU = DLL(-1, -1)
        self.LRU = DLL(-1, -1)
        self.MRU.next = self.LRU
        self.LRU.prev = self.MRU


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
        
        node = DLL(key, value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.cap:
            node_to_remove = self.LRU.prev
            self.remove(node_to_remove)
            del self.cache[node_to_remove.key]
    
    def remove(self, node):
        next = node.next
        prev = node.prev
        prev.next = next
        next.prev = prev


    def add(self, node):
        next_node = self.MRU.next
        node.next = next_node
        node.prev = self.MRU
        self.MRU.next = node
        next_node.prev = node
        
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)