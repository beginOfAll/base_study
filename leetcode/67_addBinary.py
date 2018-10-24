class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        from itertools import zip_longest
        carry = 0
        c = zip_longest(reversed(a), reversed(b), fillvalue=0)
        res = ''
        for i in c:
            tsum = int(i[0]) + int(i[1]) + carry
            if tsum > 1:
                carry = 1
                res += str(tsum - 2)
            else:
                carry = 0
                res += str(tsum)
        if carry == 1:
            res += '1'
        return res[::-1]


s = Solution()
res = s.addBinary('10', '10')
print(res)
a = int('10', 2) + int('10', 2)
b = bin(a)
print(b)
