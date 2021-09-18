from collections import defaultdict, Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counter = Counter()
        max_frequency = 0
        ans = 0

        for right, cur_char in enumerate(s):
            counter[cur_char] += 1
            max_frequency = max(max_frequency, counter[cur_char])

            while (right - left + 1) - max_frequency > k:
                counter[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans



if __name__ == "__main__":
    s = "AAAA"
    k = 0
    print(Solution().characterReplacement(s, k))
