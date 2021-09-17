from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ans = 0

        for ind in range(1, len(arr) - 1):

            if arr[ind - 1] < arr[ind] > arr[ind + 1]:

                left, right = ind, ind

                while left - 1 >= 0 and arr[left] > arr[left - 1]:
                    left -= 1

                while right + 1 < len(arr) and arr[right] > arr[right + 1]:
                    right += 1

                ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    arr = [1, 100, 2, 3, 4, 5, 6, 5, 4, 3, 2]
    print(Solution().longestMountain(arr))
