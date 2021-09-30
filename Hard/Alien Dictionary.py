from typing import List
from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def get_order(word1, word2):
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    return True, char1, char2

            if len(word1) > len(word2):
                return False, '', ''
            else:
                return True, '', ''

        adj_list = defaultdict(set)
        in_edges = {char: 0 for word in words for char in word}

        for ind in range(len(words) - 1):
            is_valid, src_letter, dst_letter = get_order(words[ind], words[ind + 1])

            if not is_valid:
                return ''
            if src_letter == '' or dst_letter == '' or dst_letter in adj_list[src_letter]:
                continue

            in_edges[src_letter] += 0
            in_edges[dst_letter] += 1
            adj_list[src_letter].add(dst_letter)

        queue = deque([char for char, count in in_edges.items() if count == 0])
        ans = ''

        while queue:
            independent_char = queue.popleft()
            ans += independent_char

            for dependent_char in adj_list[independent_char]:
                in_edges[dependent_char] -= 1
                if in_edges[dependent_char] == 0:
                    queue.append(dependent_char)

        return ans if len(in_edges) == len(ans) else ''


if __name__ == '__main__':
    words = ["ac","ab","zc","zb"]
    print(Solution().alienOrder(words))
