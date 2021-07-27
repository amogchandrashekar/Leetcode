from functools import lru_cache


class Solution:
    def minimumDistance(self, word: str) -> int:
        word_length = len(word)

        def distance(char_a: str, char_b: str) -> int:
            if not char_a or not char_b:
                # return 0 for the first letter
                return 0

            index_a = ord(char_a) - ord('A')
            index_b = ord(char_b) - ord('A')

            return abs(index_a // 6 - index_b // 6) + abs(index_a % 6 - index_b % 6)

        @lru_cache(maxsize=None)
        def find(ind: int, key_a: str, key_b: str) -> int:
            # boundary condition
            if ind == word_length:
                return 0

            char = word[ind]

            return min(
                find(ind + 1, key_a, char) + distance(key_b, char),
                find(ind + 1, char, key_b) + distance(key_a, char)
            )

        return find(0, None, None)


if __name__ == '__main__':
    word = "A" * 300
    print(Solution().minimumDistance(word))