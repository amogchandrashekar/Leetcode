from random import randint


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = dict()
        self.arr = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hash_map:
            return False
        self.hash_map[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hash_map:
            return False
        ind = self.hash_map.pop(val)
        swap_ind = len(self.arr) - 1
        self.arr[ind], self.arr[swap_ind] = self.arr[swap_ind], self.arr[ind]
        self.arr.pop()
        if ind < len(self.arr):
            self.hash_map[self.arr[ind]] = ind
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        random_ind = randint(0, len(self.arr) - 1)
        return self.arr[random_ind]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    rset = RandomizedSet()
    print(rset.remove(0))
    print(rset.remove(0))
    print(rset.insert(0))
    print(rset.getRandom())
    print(rset.remove(0))
    print(rset.insert(0))