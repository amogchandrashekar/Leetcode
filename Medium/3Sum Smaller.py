from typing import List


class Solution:
    def threeSumSmaller(self, nums, target):
        ans = 0
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            prev_ans = ans  # for pruning
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    ans += (k - j)
                    j += 1
                else:
                    k -= 1
            if prev_ans == ans:
                break  # if the ans doesn't change, then larger i won't change ans either
        return ans


if __name__ == '__main__':
    nums = [-2, 0, 1, 3]
    target = 2
    print(Solution().threeSumSmaller(nums, target))