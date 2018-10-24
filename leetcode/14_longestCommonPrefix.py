class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        prefixList = None
        for i in strs:
            if prefixList is None:
                prefixList = list(i)
            elif len(prefixList) == 0:
                return ''
            else:
                for index, value in enumerate(prefixList):
                    if index < len(i):
                        if value != i[index]:
                            prefixList = prefixList[0:index]
                            break
                    else:
                        prefixList = prefixList[0:index]
        return ''.join(prefixList)

    def longestCommonPrefix2(self, strs):
        if len(strs) == 0:
            return ''
        for index, value in enumerate(zip(*strs)):
            if len(set(value)) > 1:
                return strs[0][0:index]
        return min(strs)


strs = ['a', 'b']
s = Solution()
res = s.longestCommonPrefix2(strs)
print(res)
