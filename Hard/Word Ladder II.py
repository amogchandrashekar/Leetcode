from typing import List
from collections import defaultdict, deque
import collections
from string import ascii_lowercase


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        seen = set()
        adj_set = defaultdict(set)

        for word in wordList:
            for ind in range(len(word)):
                starred_word = word[:ind] + "*" + word[ind + 1:]
                adj_set[starred_word].add(word)

        queue = dict()
        queue[beginWord] = [[beginWord]]
        seen.add(beginWord)

        while queue:
            next_level = defaultdict(list)

            for word, paths in queue.items():

                if word == endWord:
                    return paths

                for ind in range(len(word)):
                    starred_word = word[:ind] + "*" + word[ind + 1:]
                    neighbours = adj_set[starred_word] - seen
                    for neighbour in neighbours:
                        for path in paths:
                            next_level[neighbour].append(path + [neighbour])

            seen |= set(next_level.keys())
            queue = next_level

        return []


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().findLadders(beginWord, endWord, wordList))
