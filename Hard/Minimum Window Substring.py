import collections


class Solution:
    def minWindow(self, searchString, t):
        left, right = 0, 0
        min_len = float('inf')
        ans = ''

        count = 0
        counter_search = collections.Counter()
        counter_target = collections.Counter(t)

        while right < len(searchString):
            cur_letter = searchString[right]
            counter_search[cur_letter] += 1

            if cur_letter in counter_target and counter_search[cur_letter] <= counter_target[cur_letter]:
                count += 1

            while count == len(t) and left <= right:
                if min_len > right - left + 1:
                    min_len = right - left + 1
                    ans = searchString[left: right + 1]

                removed_char = searchString[left]
                counter_search[removed_char] -= 1
                if removed_char in counter_target and counter_search[removed_char] < counter_target[removed_char]:
                    count -= 1
                left += 1

            right += 1

        return ans


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))