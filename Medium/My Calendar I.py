import bisect


class Node(object):
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.left = None
        self.right = None

    def insert(self, start, end):
        if self.e <= start:
            if not self.right:
                self.right = Node(start, end)
                return True
            else:
                return self.right.insert(start, end)
        elif self.s >= end:
            if not self.left:
                self.left = Node(start, end)
                return True
            else:
                return self.left.insert(start, end)
        else:
            return False


class MyCalendar(object):

    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = Node(start, end)
            return True

        return self.root.insert(start, end)


class MyCalendar_bs(object):

    def __init__(self):
        self.books = [[float('-inf'), float('-inf')], [float('inf'), float('inf')]]

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect(self.books, [start, end])
        if start < self.books[idx-1][1] or end > self.books[idx][0]:
            return False
        bisect.insort(self.books, [start, end])
        return True


if __name__ == "__main__":
    cal = MyCalendar_bs()
    print(cal.book(10, 20))
    print(cal.book(2, 4))
    print(cal.book(6, 8))
    print(cal.book(10, 12))
    print(cal.book(25, 30))
    print(cal.book(0, 1))
