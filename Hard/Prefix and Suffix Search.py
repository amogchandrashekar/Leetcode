from typing import List


class Trie:

    def __init__(self, index=None):
        self.children = dict()
        self.index = index

    def add_word(self, word, index):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = Trie()
            cur.index = index
            cur = cur.children[char]
        cur.index = index

    def search(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                return -1
            cur = cur.children[char]
        return cur.index


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word_ind, word in enumerate(words):
            for ind in range(len(word)):
                self.trie.add_word(word[ind:] + '#' + word, word_ind)

    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.search(suffix + '#' + prefix)


if __name__ == '__main__':
    words = ["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa", "accabaccaa", "cabcbbbcca", "ababccabcb",
       "caccbbcbab", "bccbacbcba"]
    queries = [["bccbacbcba", "a"], ["ab", "abcaccbcaa"], ["a", "aa"], ["cabaaba", "abaaaa"],
     ["cacc", "accbbcbab"], ["ccbcab", "bac"], ["bac", "cba"], ["ac", "accabaccaa"], ["bcbb", "aa"],
     ["ccbca", "cbcababac"]]

    wf = WordFilter(words)
    for prefix, suffix in queries:
        print(wf.f(prefix, suffix))