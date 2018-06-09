# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# Note that the row index starts from 0.

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        b = []
        c = []
        for i in range(rowIndex+1):
            a = []
            for j in range(i + 1):
                a.append(1)
            b.append(a)

        for j in range(rowIndex+1):
            if j > 1:
                for k in range(len(b[j]) - 2):
                    b[j][k + 1] = b[j - 1][k] + b[j - 1][k + 1]
            c.append(b[j])

        return c[rowIndex]