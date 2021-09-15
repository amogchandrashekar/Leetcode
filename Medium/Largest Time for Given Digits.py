from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        self.valid_date = list()

        def is_valid_date(combination):
            res = ''
            for ind in combination:
                res += str(arr[ind])

            hours, minute = int(res[:2]), int(res[2:])
            if hours <= 23 and minute <= 59:
                return True, res
            return False, res

        def dfs(combination):

            if len(combination) == 4:
                is_valid, text_str = is_valid_date(combination)
                if is_valid:
                    self.valid_date.append(text_str)

            for i in range(4):
                if i not in combination:
                    dfs(combination + [i])

        dfs([])
        if len(self.valid_date) == 0:
            return ''

        self.valid_date.sort()
        max_date = self.valid_date[-1]

        return f'{max_date[:2]}:{max_date[2:]}'


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(Solution().largestTimeFromDigits(arr))
