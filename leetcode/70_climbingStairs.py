class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(n // 2 + 1):
            res += self.c(n - i, i)
        return int(res)

    def c(self, n, r):
        import math
        if r == 0 or n == 0:
            return 1
        return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
