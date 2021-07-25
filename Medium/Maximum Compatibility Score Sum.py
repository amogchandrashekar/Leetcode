from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        memo = dict()
        length = len(students)
        init_mask = (2 ** length) - 1

        def compatibility(arr1, arr2):
            ans = 0
            for num1, num2 in zip(arr1, arr2):
                if num1 == num2:
                    ans += 1
            return ans

        comp = dict()
        for s in range(length):
            for m in range(length):
                comp[(s, m)] = compatibility(students[s], mentors[m])

        def dfs(ind, mentor_mask):
            if mentor_mask == 0:
                return 0

            if (ind, mentor_mask) in memo:
                return memo[(ind, mentor_mask)]

            max_score = 0
            for i in range(ind + 1, length):
                for j in range(length):
                    if not mentor_mask & (1 << j):
                        continue
                    max_score = max(max_score, comp[(i, j)] + dfs(i, mentor_mask ^ (1 << j)))

            memo[(ind, mentor_mask)] = max_score

            return max_score

        return dfs(-1, init_mask)


if __name__ == '__main__':
    students = [[0, 0, 1, 1, 1, 0, 1], [0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1]]
    mentors = [[0, 1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 0, 0]]
    print(Solution().maxCompatibilitySum(students, mentors))