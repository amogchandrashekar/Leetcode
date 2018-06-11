# Reverse bits of a given 32 bits unsigned integer.
#
# Example:
#
# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as 00000010100101000001111010011100,
#              return 964176192 represented in binary as 00111001011110000010100101000000.
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans=bin(n)[2:]
        i=len(ans)
        while i<32:
            ans='0'+ans
            i+=1
        ans=ans[::-1]
        return int(ans,2)

# print(Solution().reverseBits(43261596))
