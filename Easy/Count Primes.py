class Solution:

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        prime = n * [True]
        prime[0] = False
        prime[1] = False
        for i in range(2,int(n**0.5)+2):
            if prime[i]:
                prime[i*i:n:i]=len(prime[i*i:n:i])*[False]
        return sum(prime)
