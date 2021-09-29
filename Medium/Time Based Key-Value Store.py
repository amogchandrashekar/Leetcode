from collections import defaultdict
from bisect import bisect_left, bisect_right


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_map = defaultdict(list)

    def bin_search(self, arr, timestamp):
        ans = -1
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_timestamp = arr[mid][0]

            if timestamp < mid_timestamp:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1

        return ans

    def set(self, key: str, value: str, timestamp: int) -> None:
        # time_map[foo] = [[1, bar]]
        if len(self.time_map[key]) == 0 or self.time_map[key][-1][0] != timestamp:
            self.time_map[key].append([timestamp, value])
        else:
            self.time_map[key][-1][1] = value

    def get(self, key: str, timestamp: int) -> str:
        if len(self.time_map[key]) == 0 or self.time_map[key][0][0] > timestamp:
            return ''
        else:
            index = self.bin_search(self.time_map[key], timestamp)
            return self.time_map[key][index][1]


if __name__ == '__main__':
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)
    print(timeMap.get("foo", 1))
    print(timeMap.get("foo", 3))
    timeMap.set("foo", "bar2", 4)
    print(timeMap.get("foo", 4))
    print(timeMap.get("foo", 5))
