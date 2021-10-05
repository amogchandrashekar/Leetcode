class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [Node() for _ in range(1000)]

    def hashcode(self, key):
        size = len(self.data)
        return key % size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashcode = self.hashcode(key)
        head = self.data[hashcode]
        while head.next:
            if head.next.key == key:
                head.next.val = value
                return
            head = head.next
        head.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashcode = self.hashcode(key)
        head = self.data[hashcode]
        while head.next:
            if head.next.key == key:
                return head.next.val
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashcode = self.hashcode(key)
        head = self.data[hashcode]

        while head.next:
            if head.next.key == key:
                toremove = head.next
                head.next = toremove.next
                toremove.next = None
                return
            head = head.next


class Node:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


if __name__ == '__main__':
    hash_map = MyHashMap()
    hash_map.put(1, 1)
    hash_map.put(1, 3)