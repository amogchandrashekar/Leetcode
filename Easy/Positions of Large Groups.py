from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i, j = 0, 0
        res = list()

        while j < len(s):
            while j < len(s) and s[i] == s[j]:
                j += 1

            if j - i >= 3:
                res.append([i, j - 1])

            i = j

        return res

