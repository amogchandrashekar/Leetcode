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


from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        """
        Using an ordered dictionary to keep track of items in the cache
        """
        self.queue = OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        """
        If key is not present in the cache, return -1
        If present, bring it to the beginning of the queue and return the value
        """
        if key in self.queue:
            self.queue.move_to_end(key, last=False)
            return self.queue[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        If Key is already present in the cache, update the value
        If not present, and size of cache is full, remove the last used element and insert this key at the beginning
        cache is not full, insert the key at the beginning
        """
        if len(self.queue) == self.size and key not in self.queue:
            self.queue.popitem()
        self.queue[key] = value
        self.queue.move_to_end(key, last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)