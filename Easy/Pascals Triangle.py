# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above i

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        b = []
        c = []
        for i in range(numRows):
            a = []
            for j in range(i + 1):
                a.append(1)
            b.append(a)

        for j in range(numRows):
            if j > 1:
                for k in range(len(b[j]) - 2):
                    b[j][k + 1] = b[j - 1][k] + b[j - 1][k + 1]
            c.append(b[j])

        return c