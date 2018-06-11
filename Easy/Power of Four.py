# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example:
# Given num = 16, return true. Given num = 5, return false.

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(num<=0):
            return False
        while(num>1):
            if(num%4==0):
                num=num/4
            else:
                return False
        return True