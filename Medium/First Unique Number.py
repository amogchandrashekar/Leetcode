"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue,
and returns -1 if there is no such integer.
void add(int value) insert value to the queue.

Example 1:

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output:
[null,2,null,2,null,3,null,-1]

Explanation:
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

"""

from typing import List
from collections import OrderedDict


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.hash_table = OrderedDict()
        self.non_unique = set()
        self.create_unique(nums)

    def create_unique(self, nums):
        for index, num in enumerate(nums):
            if num not in self.non_unique and num not in self.hash_table:
                self.hash_table[num] = index
            else:
                self.non_unique.add(num)
                if num in self.hash_table:
                    self.hash_table.pop(num)

    def showFirstUnique(self) -> int:
        if self.hash_table:
            return list(self.hash_table)[0]
        return -1

    def add(self, value: int) -> None:
        if value not in self.non_unique and value not in self.hash_table:
            self.hash_table[value] = -1
        else:
            self.non_unique.add(value)
            if value in self.hash_table:
                self.hash_table.pop(value)


if __name__ == "__main__":
    firstUnique = FirstUnique([2, 3, 5])
    print(firstUnique.showFirstUnique())
    firstUnique.add(5)
    print(firstUnique.showFirstUnique())
    firstUnique.add(2)
    print(firstUnique.showFirstUnique())
    firstUnique.add(3)
    print(firstUnique.showFirstUnique())