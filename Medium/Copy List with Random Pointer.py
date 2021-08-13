"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        hash_map = dict()
        first_pass = second_pass = head

        while first_pass:
            hash_map[first_pass] = Node(first_pass.val)
            first_pass = first_pass.next

        while second_pass:
            copied_node = hash_map[second_pass]
            if second_pass.next in hash_map:
                copied_node.next = hash_map[second_pass.next]

            if second_pass.random in hash_map:
                copied_node.random = hash_map[second_pass.random]
            second_pass = second_pass.next

        return hash_map[head] if head in hash_map else None
