from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_hash = defaultdict(list)

        # use hash map to figure out all possible one char replacements
        for word in wordList:
            for ind in range(len(word)):
                word_hash[word[:ind] + "*" + word[ind + 1:]].append(word)

        queue = deque([(beginWord, 1)])
        seen = set()
        seen.add(beginWord)

        # bfs on words
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist

            for ind in range(len(word)):
                for w in word_hash[word[:ind] + "*" + word[ind + 1:]]:
                    if w in seen:
                        continue

                    queue.append([w, dist + 1])
                    seen.add(w)

        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().ladderLength(beginWord, endWord, wordList))
