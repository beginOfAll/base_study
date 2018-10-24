class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            minus = -1
            res_int = int(str(x)[:0:-1])
        else:
            minus = 1
            res_int = int(str(x)[::-1])
        if res_int > 2147483647:
            res_int = 0
        return res_int * minus


s = Solution()
res = s.reverse(-5345)
print(res)

## 反转一个int，保留负号
