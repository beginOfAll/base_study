class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if haystack == "":
            return -1
        length = len(needle)
        firstCode = needle[0]
        for i in range(len(haystack) - length + 1):
            if haystack[i] == firstCode:
                if haystack[i:i + length] == needle:
                    return i
        return -1


s = Solution()
res = s.strStr("hello", "ll")
print(res)
