from typing import List
from collections import defaultdict


class LockingTree:

    def __init__(self, parent: List[int]):
        self.locked = dict()
        self.parent = parent
        self.adj_list = defaultdict(list)
        for ind, node in enumerate(self.parent):
            self.adj_list[node].append(ind)

    def is_locked(self, node):
        return node in self.locked

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locked or self.locked[num] != user:
            return False
        self.locked.pop(num)
        return True

    def check_if_child_booked(self, node):
        stack = [node]

        while stack:
            node = stack.pop()
            for child in self.adj_list[node]:
                if self.is_locked(child):
                    return True
                stack.append(child)

        return False

    def has_locked_ancestor(self, node):
        stack = [node]

        while stack:
            node = stack.pop()
            parent = self.parent[node]
            if self.is_locked(parent):
                return True
            if parent > 0:
                stack.append(parent)
        return False

    def unlock_descendents(self, node):
        stack = [node]

        while stack:
            node = stack.pop()
            for child in self.adj_list[node]:
                if self.is_locked(child):
                    self.locked.pop(child)
                stack.append(child)

    def upgrade(self, num: int, user: int) -> bool:
        if self.is_locked(num) or not self.check_if_child_booked(num) or self.has_locked_ancestor(num):
            return False

        self.lock(num, user)
        self.unlock_descendents(num)
        return True


if __name__ == '__main__':
    lockingTree = LockingTree([-1, 0, 0, 1, 1, 2, 2])
    lockingTree.lock(2, 2)
    lockingTree.unlock(2, 3)
    lockingTree.unlock(2, 2)
    lockingTree.lock(4, 5)
    lockingTree.upgrade(0, 1)
    lockingTree.lock(0, 1)