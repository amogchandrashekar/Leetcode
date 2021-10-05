from collections import defaultdict
from random import randint


class RandomizedCollection:

    def __init__(self):
        self.hash_map = defaultdict(set)
        self.arr = list()

    def insert(self, val: int) -> bool:
        return_val = val not in self.hash_map
        self.hash_map[val].add(len(self.arr))
        self.arr.append(val)
        return return_val

    def remove(self, val: int) -> bool:
        return_val = val in self.hash_map
        if val in self.hash_map:
            pop_ind = self.hash_map[val].pop()
            swap_ind = len(self.arr) - 1
            self.arr[swap_ind], self.arr[pop_ind] = self.arr[pop_ind], self.arr[swap_ind]
            self.arr.pop()
            if pop_ind < len(self.arr):
                updated_val = self.arr[pop_ind]
                self.hash_map[updated_val].remove(swap_ind)
                self.hash_map[updated_val].add(pop_ind)
            if not self.hash_map[val]:
                self.hash_map.pop(val)
        return return_val

    def getRandom(self) -> int:
        random_ind = randint(0, len(self.arr) - 1)
        return self.arr[random_ind]