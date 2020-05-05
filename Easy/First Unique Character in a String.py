from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for letter, occurance in counter.items():
            if occurance == 1:
                return s.find(letter)
        return -1


if __name__ == "__main__":
    s = 'loveleetcode'
    print(Solution().firstUniqChar(s))