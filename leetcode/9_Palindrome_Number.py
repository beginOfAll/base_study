class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x > 9 and x % 10 == 0):
            return False
        reverse_int = int(str(x)[::-1])
        if x == reverse_int:
            return True
        else:
            return False

## 判断一个int 是否回文数  123->321
