from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        counter_to_sort = [[count, char] for char, count in counter.items()]
        counter = sorted(counter_to_sort, key=lambda x: -x[0])

        res = [None] * len(s)
        wptr = 0

        for count, char in counter:
            if count > ((len(s) + 1) // 2):
                return ''
            for _ in range(count):
                res[wptr] = char
                wptr += 2

                # reset the counter
                if wptr >= len(s):
                    wptr = 1

        return ''.join(res)


if __name__ == '__main__':
    s = "aab"
    print(Solution().reorganizeString(s))