class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums.sort()
        # b = []
        #
        # for i in range(len(nums) - 2):
        #     j = i + 1
        #     k = len(nums) - 1
        #
        #     while(j<k):
        #         a=[]
        #         x=nums[i] + nums[j] + nums[k]
        #         if ( x== 0):
        #             a.append(nums[i])
        #             a.append(nums[j])
        #             a.append(nums[k])
        #             j=j+1
        #             if a not in b:
        #                 b.append(a)
        #
        #
        #         elif x > 0:
        #             k = k - 1
        #
        #         else:
        #             j = j + 1
        #
        #
        # return b

        results = []
        nums.sort()
        r = len(nums) - 1
        for i in range(len(nums) - 2):
            l = i + 1
            while (l < r):
                sum_ = nums[i] + nums[l] + nums[r]
                if (sum_ < 0):
                    l = l + 1
                elif (sum_ > 0):
                    r = r - 1
                else:
                    result = []
                    # 0 is False in a boolean context
                    result.append([nums[i], nums[l], nums[r]])
                    if result not in results:
                        results.append(result)
                    l = l + 1

Solution().threeSum([1,2,3,0,1,-1,-2,-3])