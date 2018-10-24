class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()[::-1]
        if s == "":
            return 0
        for index, value in enumerate(s):
            if value == " ":
                return index
        return len(s)
