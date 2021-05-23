from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = min(minJump, len(s) - 1)

        while q:
            ind = q.popleft()
            for i in range(max(ind + minJump, farthest + 1), min(ind + maxJump + 1, len(s))):
                if s[i] == '0':
                    q.append(i)
                farthest = max(farthest, i)

        return farthest == len(s) - 1 and s[-1] == '0'


if __name__ == '__main__':
    s = "01"
    minJump = 1
    maxJump = 1
    print(Solution().canReach(s, minJump, maxJump))