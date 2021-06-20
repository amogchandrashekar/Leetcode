from bisect import bisect_left, bisect, bisect_right


class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        a = []
        for i in range(0, 24):
            a += [i * 100 + 0, i * 100 + 15, i * 100 + 30, i * 100 + 45]

        start, finish = int(startTime.replace(":", "")), int(finishTime.replace(":", ""))
        ind = bisect_left(a, start)
        if finish < start:
            ans = a[ind:]
            end_ind = bisect_right(a, finish)
            ans += a[:end_ind]
        else:
            end_ind = bisect_right(a, finish)
            ans = a[ind: end_ind]

        return len(ans) - 1


if __name__ == '__main__':
    startTime = "12:01"
    finishTime = "12:44"
    print(Solution().numberOfRounds(startTime, finishTime))