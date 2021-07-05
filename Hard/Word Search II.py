from typing import List


class Trie:

    def __init__(self):
        self.children = {}
        self.word = ''

    def add_word(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = Trie()
            cur = cur.children[char]
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.add_word(word)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c, trie_node):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visit or board[r][c] not in trie_node.children:
                return

            visit.add((r, c))
            char = board[r][c]
            node = trie_node.children[char]
            if node.word:
                res.add(node.word)

            for dx, dy in directions:
                dfs(r + dx, c + dy, node)

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return list(res)


if __name__ == '__main__':
    board = [["a","b"],["c","d"]]
    words = ["abcb"]
    print(Solution().findWords(board, words))