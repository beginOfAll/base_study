class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars1 = {'{', '[', '('}
        chars2 = {'}': '{', ']': '[', ')': '('}
        chars = []
        for i in s:
            if i in chars1:
                chars.append(i)
            elif i in chars2:
                if not chars:
                    return False
                if chars2[i] == chars[-1]:
                    chars.pop()
                else:
                    return False
        return True if not chars else False
