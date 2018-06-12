class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = {2,3,5,7,11,13,17,19,23,29}
        count = 0
        for i in range(L, R+1):
            cur_i = bin(i).count('1')
            if cur_i in primes:
                count += 1
        return count   


print(Solution().countPrimeSetBits(6,10))