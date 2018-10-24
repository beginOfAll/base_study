class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 1:
            return "1"
        beforNum = str(self.countAndSay(n - 1))
        code = beforNum[0]
        count = 0
        resStr = ""
        for value in beforNum:
            if value != code:
                resStr = resStr + str(count) + code
                code = value
                count = 1
            else:
                count += 1
        resStr = resStr + str(count) + code
        return resStr
