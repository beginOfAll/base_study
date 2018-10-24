class Solution:
    def plusOne(self, digits):
        """
        :type digits: list[int]
        :rtype: list[int]
        """
        carry = None
        for i in reversed(range(len(digits))):
            if carry is None:
                digits[i] += 1
            else:
                digits[i] += carry
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
        if carry == 1:
            digits.insert(0, 1)
        return digits


s = Solution()
res = s.plusOne([1, 0])
print(res)
