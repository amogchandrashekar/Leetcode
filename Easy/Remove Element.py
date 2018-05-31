class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.sort()
        i=len(nums)-1
        while(i>=0):
            if(nums[i]==val):
                nums.pop(i)
                i=i-1
            else:
                i=i-1

        return len(nums)

print(Solution().removeElement([1,1,1,1,2,2,2,3],1))
