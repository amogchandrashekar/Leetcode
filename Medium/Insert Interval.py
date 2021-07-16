from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: (x[0], x[1]))

        merged_intervals = list()
        for start, end in intervals:
            # merge intervals if overlapping
            if merged_intervals and merged_intervals[-1][-1] >= start:
                merged_intervals[-1][-1] = max(merged_intervals[-1][-1], end)
            else:
                merged_intervals.append([start, end])

        return merged_intervals