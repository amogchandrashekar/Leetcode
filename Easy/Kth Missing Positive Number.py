from typing import List


class Solution:
    def findKthPositive(self, arr, k):
        beg, end = 0, len(arr)
        while beg < end:
            mid = (beg + end) // 2
            if arr[mid] - mid - 1 < k:
                beg = mid + 1
            else:
                end = mid
        return end + k


if __name__ == '__main__':
    arr = [2, 3, 4, 7, 11]
    k = 5
    print(Solution().findKthPositive(arr, k))
