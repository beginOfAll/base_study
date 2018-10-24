class Solution:
    def mySqrt(self, x):
        """
        :type x:
        :rtype: int
        """
        if x < 2:
            return x
        begin = 0
        end = x
        while True:
            mid = (begin + end) // 2
            if mid ** 2 <= x and (mid + 1) ** 2 > x:
                return mid
            if mid ** 2 < x:
                begin = mid
            else:
                end = mid
