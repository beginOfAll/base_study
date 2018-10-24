class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        befor = None
        val = 0
        i = 0
        length = len(nums)
        while i < length:
            val = nums[i]
            if befor is None:
                befor = val
                i += 1
            else:
                if val == befor:
                    nums.pop(i)
                    length -= 1
                else:
                    befor = val
                    i += 1
        return len(nums)


l = [1, 1, 2]
s = Solution()
res = s.removeDuplicates(l)
print(res)
