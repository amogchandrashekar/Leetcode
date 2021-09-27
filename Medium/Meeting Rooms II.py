from collections import Counter
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        interval_counter = Counter()

        for start, end in intervals:
            interval_counter[start] += 1
            interval_counter[end] -= 1

        sorted_intervals = sorted(list(interval_counter.keys()))

        max_overlapping, cur_overlapping = 0, 0

        for interval in sorted_intervals:
            cur_overlapping += interval_counter[interval]
            max_overlapping = max(max_overlapping, cur_overlapping)

        return max_overlapping