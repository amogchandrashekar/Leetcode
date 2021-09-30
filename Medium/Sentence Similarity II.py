from typing import List
from collections import defaultdict


class DSU:

    def __init__(self):
        self.parent = defaultdict(dict)

    def find(self, node):
        if node not in self.parent:
            self.parent[node] = node

        parent = self.parent[node]
        while parent != self.parent[parent]:
            self.parent[parent] = self.parent[self.parent[parent]]
            parent = self.parent[parent]
        return parent

    def union(self, nodea, nodeb):
        parent_a, parent_b = self.find(nodea), self.find(nodeb)
        if parent_a == parent_b:
            return
        self.parent[parent_b] = parent_a


class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        dsu = DSU()
        for word, similar_word in similarPairs:
            dsu.union(word, similar_word)

        for word_s1, word_s2 in zip(sentence1, sentence2):
            if word_s1 != word_s2 and dsu.find(word_s1) != dsu.find(word_s2):
                return False

        return True


if __name__ == '__main__':
    sentence1 = ["I", "love", "leetcode"]
    sentence2 = ["I", "love", "onepiece"]
    similarPairs = [["manga", "onepiece"], ["platform", "anime"], ["leetcode", "platform"], ["anime", "manga"]]
    print(Solution().areSentencesSimilarTwo(sentence1, sentence2, similarPairs))
