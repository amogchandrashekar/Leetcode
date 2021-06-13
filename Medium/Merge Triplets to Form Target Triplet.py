from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = float('-inf'), float('-inf'), float('-inf')
        targ_a, targ_b, targ_c = target

        for ind, triplet in enumerate(triplets):
            trip_a, trip_b, trip_c = triplets[ind]
            if trip_a > targ_a or trip_b > targ_b or trip_c > targ_c:
                continue
            a = max(a, trip_a)
            b = max(b, trip_b)
            c = max(c, trip_c)

        return [a, b, c] == target


if __name__ == '__main__':
    triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
    target = [2, 7, 5]
    print(Solution().mergeTriplets(triplets, target))

