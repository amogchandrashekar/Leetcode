from typing import List
from collections import defaultdict


class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # via this mapping, we can easily know which coordinates should be took into consideration.
        mapping = defaultdict(int)
        for s, e, c in segments:
            mapping[s] += c
            mapping[e] -= c

        res = []
        prev, color = None, 0
        sorted_color = sorted(mapping)

        for now in sorted_color:
            if prev is not None and color != 0:  # if color == 0, it means this part isn't painted.
                res.append([prev, now, color])

            color += mapping[now]
            prev = now

        return res


if __name__ == '__main__':
    segments = [[1, 7, 9], [6, 8, 15], [8, 10, 7]]
    print(Solution().splitPainting(segments))