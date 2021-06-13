from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def is_sub(ind_a, ind_b):
            """
            Check if its a substring
            """
            while ind_a < len(s) and ind_b < len(p):
                if ind_a in removed or s[ind_a] != p[ind_b]:
                    ind_a += 1
                    continue
                ind_a += 1
                ind_b += 1
            return ind_b == len(p)

        min_rem = 0

        left, right = 0, len(removable) - 1
        while left <= right:
            """
            Use binary search to accelerate the search
            """
            mid = (left + right) // 2
            removed = set(removable[:mid + 1])
            if is_sub(0, 0):
                min_rem = max(mid + 1, min_rem)
                left = mid + 1
            else:
                right = mid - 1

        return min_rem


if __name__ == '__main__':

    s = "abcacb"
    p = "ab"
    removable = [3, 1, 0]

    print(Solution().maximumRemovals(s, p, removable))