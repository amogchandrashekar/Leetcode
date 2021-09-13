from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s)
        counter_t = Counter(t)

        for elem, count in counter_t.items():
            if counter_s[elem] != count:
                return elem
