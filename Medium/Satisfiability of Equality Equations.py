from typing import List
from collections import defaultdict


class DSU:

    def __init__(self):
        self.parents = defaultdict(dict)

    def find(self, node):
        if node not in self.parents:
            self.parents[node] = node
        parent = self.parents[node]
        while parent != self.parents[parent]:
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        return parent

    def union(self, nodea, nodeb):
        par_a, par_b = self.find(nodea), self.find(nodeb)

        if par_a == par_b:
            return

        self.parents[par_b] = par_a


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU()

        for equation in equations:
            if '==' in equation:
                var_a, var_b = equation.split('==')
                dsu.union(var_a, var_b)

        for equation in equations:
            if '!=' in equation:
                var_a, var_b = equation.split('!=')
                if dsu.find(var_a) == dsu.find(var_b):
                    return False

        return True