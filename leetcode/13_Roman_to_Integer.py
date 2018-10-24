class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
        res = 0
        bef = 'I'
        for i in reversed(s):
            if roman[i] >= roman[bef]:
                res += roman[i]
            else:
                res -= roman[i]
            bef = i
        return res


# 罗马数字转 int

s = Solution()
res = s.romanToInt("XLVII")
print(res)
