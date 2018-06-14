import itertools

from future.moves import collections


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        if not points:
            return 0
        res = 0
        for i in range(len(points) - 1):
            ha = []
            c = 0
            for j in range(i + 1, len(points)):
                if points[i].y - points[j].y == 0:
                    if points[i].x - points[j].x == 0:
                        c += 1
                    else:
                        ha.append(100000)
                else:
                    ha.append((points[i].x - points[j].x) / (points[i].y - points[j].y))
            print(ha)
            if ha == []:
                res = max(c, res)
            else:
                res = max(max(list(collections.Counter(ha).values())) + c, res)
        return res + 1


print(Solution().maxPoints([[Point(0,0),Point(1,1)]]))



