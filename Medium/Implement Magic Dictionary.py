from typing import List


class Trie:

    def __init__(self):
        self.children = dict()
        self.is_word = False

    def add_word(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word, mis_spelt, word_ind=0):
        curr = self

        if word_ind == len(word):
            return curr.is_word and mis_spelt == 0

        char = word[word_ind]
        is_match = False

        for child_char, child_trie in curr.children.items():
            if char == child_char:
                is_match = is_match or child_trie.search(word, mis_spelt, word_ind + 1)
            elif mis_spelt:
                is_match = is_match or child_trie.search(word, mis_spelt - 1, word_ind + 1)

        return is_match


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.add_word(word)

    def search(self, searchWord: str) -> bool:
        return self.trie.search(searchWord, 1)


if __name__ == '__main__':
    dictionary = MagicDictionary()
    dictionary.buildDict(["hello","leetcode", "judge", "judgg"])
    print(dictionary.search("juggg"))
    print(dictionary.search("hhllo"))
    print(dictionary.search("hell"))
    print(dictionary.search("leetcoded"))