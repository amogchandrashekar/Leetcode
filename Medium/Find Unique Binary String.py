from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        bit_length = len(nums[0])
        nums = set(nums)
        max_num = (2 ** bit_length)

        for num in range(0, max_num):
            bit_num = str(bin(num)[2:]).zfill(bit_length)
            if bit_num not in nums:
                return bit_num


if __name__ == '__main__':
    nums = ["111","011","001"]
    print(Solution().findDifferentBinaryString(nums))