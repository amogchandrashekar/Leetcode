class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        OPEN, CLOSE = 0, 1
        MOD = 10 ** 9 + 7

        events = list()
        for x1, y1, x2, y2 in rectangles:
            events.append([x1, OPEN, y1, y2])
            events.append([x2, CLOSE, y1, y2])

        total_area = 0
        events.sort()

        def merged_area_without_overlap(intervals, width):
            area = 0
            start = 0
            for y1, y2 in intervals:
                y1 = max(y1, start)
                delta = y2 - y1
                if delta > 0:
                    area += (delta * width)
                    start = y2
            return area

        intervals = list()
        prev = 0

        for x, is_opening, y1, y2 in events:
            width = x - prev
            total_area += merged_area_without_overlap(intervals, width)

            if is_opening == CLOSE:
                intervals.remove([y1, y2])
            else:
                intervals.append([y1, y2])
                intervals.sort()

            prev = x

        return total_area % MOD


if __name__ == '__main__':
    rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
    print(Solution().rectangleArea(rectangles))