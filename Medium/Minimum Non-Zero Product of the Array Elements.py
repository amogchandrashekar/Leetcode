class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        n = 2 ** p - 1
        M = 10 ** 9 + 7
        return (pow(n - 1, n // 2, M) * n) % M


if __name__ == '__main__':
    n = 3
    print(Solution().minNonZeroProduct(n))