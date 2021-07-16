from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        merged_intervals = []
        start, stop = intervals[0]

        for strt_i, stop_i in intervals[1:]:
            # merge the intervals
            if start <= strt_i <= stop:
                start = min(start, strt_i)
                stop = max(stop, stop_i)

            else:
                # create a new interval
                merged_intervals.append([start, stop])
                start, stop = strt_i, stop_i

        merged_intervals.append([start, stop])
        return merged_intervals


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))