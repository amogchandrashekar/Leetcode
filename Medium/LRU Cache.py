"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:
get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        """
        Using an ordered dictionary to keep track of items in the cache
        """
        self.capacity = capacity
        self.cache = dict()

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # inserts node to the position behind right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node

    def get(self, key: int) -> int:
        """
        If key is not present in the cache, return -1
        If present, bring it to the beginning of the queue and return the value
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        If Key is already present in the cache, update the value
        If not present, and size of cache is full, remove the last used element and insert this key at the beginning
        cache is not full, insert the key at the beginning
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            remove_elem = self.left.next
            self.remove(remove_elem)
            del self.cache[remove_elem.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    cache = LRUCache(2)
    print(cache.put(1, 1))
    print(cache.put(2, 2))
    print(cache.put(1, 3))
    print(cache.get(1))
    print(cache.put(3, 3))
    print(cache.get(2))
    print(cache.put(4, 4))
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))